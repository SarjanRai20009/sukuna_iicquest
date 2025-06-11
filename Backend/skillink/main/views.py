# skillink/views.py

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Skill, UserJobSeeker, UserSkill
from .serializers import (
    SkillSerializer,
    UserJobSeekerSerializer,
    UserSkillSerializer,
    UserJobSeekerDetailSerializer,
    LoginSerializer
)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterUserJobSeekerAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserJobSeekerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            tokens = get_tokens_for_user(user)
            return Response({
                "message": "Registration successful!",
                "user_id": user.id,
                "ujs_full_name": user.ujs_full_name,
                "ujs_username": user.ujs_username,
                "access_token": tokens['access'],
                "refresh_token": tokens['refresh']
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.context['user']

        django_login(request, user)

        response = super().post(request, *args, **kwargs)
        
        response.data['user_id'] = user.id
        response.data['ujs_full_name'] = user.ujs_full_name
        response.data['ujs_username'] = user.ujs_username
        
        return response

class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        django_logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    lookup_field = 'id'

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        skills = Skill.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
        page = self.paginate_queryset(skills)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(skills, many=True)
        return Response(serializer.data)


class UserJobSeekerViewSet(viewsets.ModelViewSet):
    queryset = UserJobSeeker.objects.all()
    serializer_class = UserJobSeekerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    lookup_field = 'id'

    def get_permissions(self):
        if self.action in ['create', 'check_username', 'check_email']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'profile']:
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

    @action(detail=False, methods=['get', 'put', 'patch'], permission_classes=[IsAuthenticated], url_path='me')
    def profile(self, request):
        user = request.user
        
        if request.method in ['PUT', 'PATCH']:
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated], url_path='me/change-password')
    def change_password(self, request):
        user = request.user 
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if not old_password or not new_password:
            return Response(
                {'detail': 'Both old_password and new_password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not user.check_password(old_password):
            return Response(
                {'old_password': 'Wrong password.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.ujs_password = new_password
        user.save()
        return Response({'status': 'password changed successfully'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put', 'patch'], permission_classes=[IsAuthenticated], url_path='me/update-interests')
    def update_interests(self, request):
        user = request.user
        areas_of_Interest = request.data.get('areas_of_Interest')

        if areas_of_Interest is None:
            return Response(
                {'areas_of_Interest': 'This field is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.areas_of_Interest = areas_of_Interest
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data)


class UserSkillViewSet(viewsets.ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def update_proficiency(self, request, id=None):
        user_skill = self.get_object()
        
        if not request.user.is_superuser and user_skill.ujs_full_name != request.user:
            return Response({'detail': 'You do not have permission to update this skill.'}, status=status.HTTP_403_FORBIDDEN)

        proficiency_level = request.data.get('proficiency_level')
        years_of_experience = request.data.get('years_of_experience')
        
        if proficiency_level is not None:
            user_skill.proficiency_level = proficiency_level
        if years_of_experience is not None:
            user_skill.years_of_experience = years_of_experience
        
        user_skill.save()
        return Response(self.get_serializer(user_skill).data, status=status.HTTP_200_OK)

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
        return Response(serializer.data, status=status.HTTP_200_OK)