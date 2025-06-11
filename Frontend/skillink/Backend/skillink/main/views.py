from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Skill, UserJobSeeker, UserSkill
from .serializers import (
    SkillSerializer,
    UserJobSeekerSerializer,
    UserSkillSerializer,
    UserJobSeekerDetailSerializer
)

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:
            return [permissions.AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def search(self, request):
       
        query = request.query_params.get('q', '')
        skills = Skill.objects.filter(name__icontains=query)
        page = self.paginate_queryset(skills)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(skills, many=True)
        return Response(serializer.data)

class UserJobSeekerViewSet(viewsets.ModelViewSet):
    queryset = UserJobSeeker.objects.all()
    serializer_class = UserJobSeekerSerializer
    permission_classes = [permissions.AllowAny]  # Allow registration without auth
    lookup_field = 'id'

    def get_permissions(self):
        if self.action in ['create', 'check_username', 'check_email']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserJobSeekerDetailSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['get'])
    def check_username(self, request):
        
        username = request.query_params.get('username', '')
        exists = UserJobSeeker.objects.filter(ujs_username__iexact=username).exists()
        return Response({'available': not exists})

    @action(detail=False, methods=['get'])
    def check_email(self, request):
       
        email = request.query_params.get('email', '')
        exists = UserJobSeeker.objects.filter(ujs_email__iexact=email).exists()
        return Response({'available': not exists})

    @action(detail=True, methods=['get', 'put', 'patch'], permission_classes=[permissions.IsAuthenticated])
    def profile(self, request, id=None):
    
        user = self.get_object()
        if request.method in ['PUT', 'PATCH']:
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def change_password(self, request, id=None):
      
        user = self.get_object()
        if not user.check_password(request.data.get('old_password')):
            return Response(
                {'old_password': 'Wrong password.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.ujs_password = make_password(request.data.get('new_password'))
        user.save()
        return Response({'status': 'password changed'})

    @action(detail=True, methods=['put', 'patch'], permission_classes=[permissions.IsAuthenticated])
    def update_interests(self, request, id=None):
       
        user = self.get_object()
        user.areas_of_Interest = request.data.get('areas_of_Interest', '')
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

class UserSkillViewSet(viewsets.ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
     
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(ujs_full_name=self.request.user)
        return queryset.select_related('skill', 'ujs_full_name')

    def perform_create(self, serializer):
        
        if not self.request.user.is_superuser:
            serializer.save(ujs_full_name=self.request.user)
        else:
            serializer.save()

    @action(detail=False, methods=['get'])
    def my_skills(self, request):
       
        user_skills = UserSkill.objects.filter(ujs_full_name=request.user)
        page = self.paginate_queryset(user_skills)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(user_skills, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def update_proficiency(self, request, id=None):
       
        user_skill = self.get_object()
        
        proficiency_level = request.data.get('proficiency_level')
        years_of_experience = request.data.get('years_of_experience')
        
        if proficiency_level is not None:
            user_skill.proficiency_level = proficiency_level
        if years_of_experience is not None:
            user_skill.years_of_experience = years_of_experience
        
        user_skill.save()
        return Response(self.get_serializer(user_skill).data)

    @action(detail=False, methods=['get'])
    def by_skill(self, request):
       
        skill_id = request.query_params.get('skill_id')
        if not skill_id:
            return Response(
                {'error': 'skill_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        skill = get_object_or_404(Skill, id=skill_id)
        user_skills = UserSkill.objects.filter(skill=skill)
        serializer = self.get_serializer(user_skills, many=True)
        return Response(serializer.data)