

# from rest_framework import viewsets, status, permissions
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from django.shortcuts import get_object_or_404
# from django.db.models import Q

# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView

# from django.contrib.auth import login as django_login, logout as django_logout
# from django.contrib.auth.hashers import make_password
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from .models import Skill, UserJobSeeker, UserSkill
# from .serializers import (
#     SkillSerializer,
#     UserJobSeekerSerializer,
#     UserSkillSerializer,
#     UserJobSeekerDetailSerializer,
#     LoginSerializer
# )

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


# class RegisterUserJobSeekerAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserJobSeekerSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
            
#             tokens = get_tokens_for_user(user)
#             return Response({
#                 "message": "Registration successful!",
#                 "user_id": user.id,
#                 "ujs_full_name": user.ujs_full_name,
#                 "ujs_username": user.ujs_username,
#                 "access_token": tokens['access'],
#                 "refresh_token": tokens['refresh']
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
        
#         try:
#             serializer.is_valid(raise_exception=True)
#         except Exception as e:
#             return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         user = serializer.context['user']
        
#         # Login the user (for session auth if needed)
#         django_login(request, user)
        
#         # Generate tokens manually
#         refresh = RefreshToken.for_user(user)
        
#         # Return response with tokens and user data
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#             'id': user.pk,
#             'ujs_full_name': user.ujs_full_name,
#             'ujs_username': user.ujs_username,
#             'ujs_email': user.ujs_email,
#             # Include other non-sensitive fields you want to return
#             # Never include ujs_password in the response!
#         }, status=status.HTTP_200_OK)

# class LogoutAPIView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         django_logout(request)
#         return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)


# class SkillViewSet(viewsets.ModelViewSet):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated] 
#     lookup_field = 'id'

#     def get_permissions(self):
#         if self.action in ['list', 'retrieve', 'search']:
#             return [AllowAny()]
#         return [IsAuthenticated()]

#     @action(detail=False, methods=['get'])
#     def search(self, request):
#         query = request.query_params.get('q', '')
#         skills = Skill.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
#         page = self.paginate_queryset(skills)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
        
#         serializer = self.get_serializer(skills, many=True)
#         return Response(serializer.data)


# class UserJobSeekerViewSet(viewsets.ModelViewSet):
#     queryset = UserJobSeeker.objects.all()
#     serializer_class = UserJobSeekerSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated] 
#     lookup_field = 'id'

#     def get_permissions(self):
#         if self.action in ['create', 'check_username', 'check_email']:
#             return [AllowAny()]
#         return [IsAuthenticated()]

#     def get_serializer_class(self):
#         if self.action in ['retrieve', 'profile']:
#             return UserJobSeekerDetailSerializer
#         return super().get_serializer_class()

#     @action(detail=False, methods=['get'])
#     def check_username(self, request):
#         username = request.query_params.get('username', '')
#         exists = UserJobSeeker.objects.filter(ujs_username__iexact=username).exists()
#         return Response({'available': not exists})

#     @action(detail=False, methods=['get'])
#     def check_email(self, request):
#         email = request.query_params.get('email', '')
#         exists = UserJobSeeker.objects.filter(ujs_email__iexact=email).exists()
#         return Response({'available': not exists})

#     @action(detail=False, methods=['get', 'put', 'patch'], permission_classes=[IsAuthenticated], url_path='me')
#     def profile(self, request):
#         user = request.user
        
#         if request.method in ['PUT', 'PATCH']:
#             serializer = self.get_serializer(user, data=request.data, partial=True)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
        
#         serializer = self.get_serializer(user)
#         return Response(serializer.data)

#     @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated], url_path='me/change-password')
#     def change_password(self, request):
#         user = request.user 
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
        
#         if not old_password or not new_password:
#             return Response(
#                 {'detail': 'Both old_password and new_password are required.'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         if not user.check_password(old_password):
#             return Response(
#                 {'old_password': 'Wrong password.'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
#         user.ujs_password = new_password
#         user.save()
#         return Response({'status': 'password changed successfully'}, status=status.HTTP_200_OK)

#     @action(detail=False, methods=['put', 'patch'], permission_classes=[IsAuthenticated], url_path='me/update-interests')
#     def update_interests(self, request):
#         user = request.user
#         areas_of_Interest = request.data.get('areas_of_Interest')

#         if areas_of_Interest is None:
#             return Response(
#                 {'areas_of_Interest': 'This field is required.'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
#         user.areas_of_Interest = areas_of_Interest
#         user.save()
#         serializer = self.get_serializer(user)
#         return Response(serializer.data)


# class UserSkillViewSet(viewsets.ModelViewSet):
#     queryset = UserSkill.objects.all()
#     serializer_class = UserSkillSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if not self.request.user.is_superuser:
#             queryset = queryset.filter(ujs_full_name=self.request.user) 
#         return queryset.select_related('skill', 'ujs_full_name')

#     def perform_create(self, serializer):
#         if not self.request.user.is_superuser:
#             serializer.save(ujs_full_name=self.request.user)
#         else:
#             serializer.save()

#     @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
#     def update_proficiency(self, request, id=None):
#         user_skill = self.get_object()
        
#         if not request.user.is_superuser and user_skill.ujs_full_name != request.user:
#             return Response({'detail': 'You do not have permission to update this skill.'}, status=status.HTTP_403_FORBIDDEN)

#         proficiency_level = request.data.get('proficiency_level')
#         years_of_experience = request.data.get('years_of_experience')
        
#         if proficiency_level is not None:
#             user_skill.proficiency_level = proficiency_level
#         if years_of_experience is not None:
#             user_skill.years_of_experience = years_of_experience
        
#         user_skill.save()
#         return Response(self.get_serializer(user_skill).data, status=status.HTTP_200_OK)

#     @action(detail=False, methods=['get'])
#     def by_skill(self, request):
#         skill_id = request.query_params.get('skill_id')
#         if not skill_id:
#             return Response(
#                 {'error': 'skill_id parameter is required'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
        
#         skill = get_object_or_404(Skill, id=skill_id)
#         user_skills = UserSkill.objects.filter(skill=skill)
#         serializer = self.get_serializer(user_skills, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib import messages 
from django.db.models.functions import Lower
from . import models

from django.template.defaulttags import register
from main import models
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.views.generic import ListView

from django.db.models import Q

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.db import IntegrityError
from django.utils.dateparse import parse_date
from django.views.generic import TemplateView
from django.views import View
from .serializers import *



from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import (
    Skill, UserJobSeeker, PortfolioItem, UserSkill, Company, Mentor, Expert,
    JobPost, NewsEvent, ChatRoom, ChatMessage, Internship, Scholarship,
    JobApplication, InternshipApplication, ScholarshipApplication
)
from .serializers import *
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Skill 
import json
import django.db.models as models
from django.core.exceptions import PermissionDenied
from .serializers import (
    SkillSerializer, UserJobSeekerSerializer, PortfolioItemSerializer, UserSkillSerializer,
    CompanySerializer, MentorSerializer, ExpertSerializer, JobPostSerializer,
    NewsEventSerializer, ChatRoomSerializer, ChatMessageSerializer, InternshipSerializer,
    ScholarshipSerializer, JobApplicationSerializer, InternshipApplicationSerializer,
    ScholarshipApplicationSerializer
)

class IndexView(TemplateView):
    template_name = 'base_template/main.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get logged-in user ID from session
        ujs_id = self.request.session.get('ujs_id')
        
        if not ujs_id:
            messages.error(self.request, 'Please login to access your dashboard.')
            return context
            
        try:
            # Fetch only the logged-in user's data
            user = UserJobSeeker.objects.get(id=ujs_id)
            context['user'] = user
            
            # Calculate age if date of birth exists
            if user.ujs_date_of_birth:
                today = timezone.now().date()
                age = today.year - user.ujs_date_of_birth.year - (
                    (today.month, today.day) < (user.ujs_date_of_birth.month, user.ujs_date_of_birth.day))
                context['user_age'] = age
            
        except UserJobSeeker.DoesNotExist:
            messages.error(self.request, 'User not found. Please login again.')
            # Clear invalid session
            if 'ujs_id' in self.request.session:
                del self.request.session['ujs_id']
            if 'ujs_username' in self.request.session:
                del self.request.session['ujs_username']
        
        return context
     
     
    
    
def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me') == 'true' # Check if 'remember_me' checkbox is ticked

        try:
            # Attempt to find the user by username
            user_job_seeker = UserJobSeeker.objects.get(ujs_username=username)

            # Check the password using the custom method on the UserJobSeeker model
            if user_job_seeker.check_password(password):
               
                request.session['ujs_id'] = user_job_seeker.id
                request.session['ujs_username'] = user_job_seeker.ujs_username

                # If "Remember Me" is checked, set a longer session expiry
                if remember_me:
                    request.session.set_expiry(60 * 60 * 24 * 30) # Session expires in 30 days
                else:
                    request.session.set_expiry(0) # Session expires when browser closes

                messages.success(request, 'Login successful!')
                # Redirect to a dashboard or home page after successful login
                return redirect('index') # Assuming you have a URL named 'index'

            else:
                # Invalid password
                messages.error(request, 'Invalid username or password.')

        except UserJobSeeker.DoesNotExist:
            # User with that username not found
            messages.error(request, 'Invalid username or password.')
        
      
        return render(request, 'auth_template/login.html', {'error_message': messages.get_messages(request)})

    else:
        # For GET request, just render the empty login form
        return render(request, 'auth_template/login.html')
class LogoutView(View):
    def get(self, request):
        """Logs out the user and redirects them to the base template."""
        logout(request)  
        return redirect('/login/')



class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Skill added successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Skill updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Skill deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
        
        
class SkillSearch(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return Skill.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return Skill.objects.none()  # Return an empty queryset if no query is provided

def register_user(request):
    if request.method == 'POST':
        try:
            # Collect data from the form
            full_name = request.POST.get('full_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            phone_number = request.POST.get('phone_number')
            dob = request.POST.get('date_of_birth')
            address = request.POST.get('address')
            gender = request.POST.get('gender')
            interests = request.POST.get('areas_of_interest')
            pan_number = request.POST.get('pan_number')
            profile_image = request.FILES.get('profile_image')

            # Save to database
            new_user = UserJobSeeker(
                ujs_full_name=full_name,
                ujs_username=username,
                ujs_email=email,
                ujs_password=password,  # Will be hashed in model save()
                ujs_phone_number=phone_number,
                ujs_date_of_birth=parse_date(dob) if dob else None,
                ujs_address=address,
                gender=gender,
                areas_of_Interest=interests,
                pan_number=pan_number,
                profile_image=profile_image
            )
            new_user.save()
            messages.success(request, 'Registration successful!')
            return redirect('register_user')  # or redirect to login/dashboard

        except IntegrityError as e:
            messages.error(request, 'Username, email, or PAN already exists.')
        except Exception as e:
            messages.error(request, f'Error during registration: {str(e)}')

    return render(request, 'auth_template/register.html')

class UserJobSeekerList(generics.ListCreateAPIView):
    queryset = UserJobSeeker.objects.all()
    serializer_class = UserJobSeekerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User Job Seeker created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserJobSeekerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserJobSeeker.objects.all()
    serializer_class = UserJobSeekerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User Job Seeker updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "User Job Seeker deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
        
    # def get_queryset(self):
       
    #     if self.request.user.is_authenticated and hasattr(self.request.user, 'userjobseeker'):
    #         return UserJobSeeker.objects.filter(id=self.request.user.userjobseeker.id)
    #     return UserJobSeeker.objects.none() # No access if not authenticated or not a job seeker

    def perform_update(self, serializer):
      
        if 'ujs_password' in self.request.data:
            serializer.validated_data['ujs_password'] = models.make_password(serializer.validated_data['ujs_password'])
        serializer.save()

class PortfolioItemList(generics.ListCreateAPIView):
    serializer_class = PortfolioItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PortfolioItem.objects.all()

    # def get_queryset(self):
    #     # Users can only see and add their own portfolio items
    #     if hasattr(self.request.user, 'userjobseeker'):
    #         return PortfolioItem.objects.filter(user=self.request.user.userjobseeker)
    #     return PortfolioItem.objects.none()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user.userjobseeker)
            return Response({
                "message": "Portfolio item created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.userjobseeker) # Associate with the current user
    

class PortfolioItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PortfolioItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        # Users can only retrieve/update/delete their own portfolio items
        if hasattr(self.request.user, 'userjobseeker'):
            return PortfolioItem.objects.filter(user=self.request.user.userjobseeker)
        return PortfolioItem.objects.none()
    def perform_create(self, serializer):
        # Ensure the portfolio item is associated with the current job seeker
        serializer.save(user=self.request.user.userjobseeker)
        
    def perform_update(self, serializer):
        if 'user' in self.request.data:
            serializer.validated_data['user'] = self.request.user.userjobseeker
        serializer.save()
    def perform_destroy(self, instance):
        if instance.user != self.request.user.userjobseeker:
            raise PermissionDenied("You do not have permission to delete this portfolio item.")
        instance.delete()
        return Response({"message": "Portfolio item deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

class UserSkillList(generics.ListCreateAPIView):
    serializer_class = UserSkillSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    

    def get_queryset(self):
        # Users can only see their own skills
        if hasattr(self.request.user, 'userjobseeker'):
            return models.UserSkill.objects.filter(ujs_full_name=self.request.user.userjobseeker)
        return models.UserSkill.objects.none()

    def perform_create(self, serializer):
        # Ensure the user skill is associated with the current job seeker
        job_seeker = self.request.user.userjobseeker
        skill = serializer.validated_data['skill']
        
        # Prevent duplicate skills for the same user
        if models.UserSkill.objects.filter(ujs_full_name=job_seeker, skill=skill).exists():
            raise serializers.ValidationError("This skill already exists for this user.")
        
        serializer.save(ujs_full_name=job_seeker)
    
        

class UserSkillDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users can only retrieve/update/delete their own skills
        if hasattr(self.request.user, 'userjobseeker'):
            return models.UserSkill.objects.filter(ujs_full_name=self.request.user.userjobseeker)
        return models.UserSkill.objects.none()
    def perform_update(self, serializer):
        # Ensure the user skill is associated with the current job seeker
        job_seeker = self.request.user.userjobseeker
        if 'ujs_full_name' in serializer.validated_data:
            serializer.validated_data['ujs_full_name'] = job_seeker
        serializer.save()
    def perform_destroy(self, instance):
        if instance.ujs_full_name != self.request.user.userjobseeker:
            raise PermissionDenied("You do not have permission to delete this skill.")
        instance.delete()
        return Response({"message": "User skill deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            company = serializer.save()
            return Response({
                "message": "Company created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Company updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Company deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class CompanySearch(generics.ListAPIView):
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return Company.objects.filter(
                Q(name__icontains=query) | Q(industry__icontains=query) | Q(email__icontains=query)
            )
        return Company.objects.none()  # Return an empty queryset if no query is provided
class MentorList(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            mentor = serializer.save()
            return Response({
                "message": "Mentor created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Mentor updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Mentor deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class ExpertList(generics.ListCreateAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            expert = serializer.save()
            return Response({
                "message": "Expert created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ExpertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Expert updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Expert deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class JobPostList(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            job_post = serializer.save()
            return Response({
                "message": "Job post created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
class JobPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Job post updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Job post deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class JobPostSearch(generics.ListAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return JobPost.objects.filter(
                Q(title__icontains=query) | Q(company__name__icontains=query) | Q(location__icontains=query)
            )
        return JobPost.objects.none()  # Return an empty queryset if no query is provided
    
class NewsEventList(generics.ListCreateAPIView):
    queryset = NewsEvent.objects.all()
    serializer_class = NewsEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            news_event = serializer.save()
            return Response({
                "message": "News/Event created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class NewsEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsEvent.objects.all()
    serializer_class = NewsEventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "News/Event updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "News/Event deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class NewsEventSearch(generics.ListAPIView):
    serializer_class = NewsEventSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return NewsEvent.objects.filter(
                Q(title__icontains=query) | Q(company__name__icontains=query) | Q(content__icontains=query)
            )
        return NewsEvent.objects.none()  # Return an empty queryset if no query is provided
class ChatRoomList(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            chat_room = serializer.save()
            return Response({
                "message": "Chat room created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ChatRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Chat room updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Chat room deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)   
class ChatMessageList(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            chat_message = serializer.save()
            return Response({
                "message": "Chat message created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
class ChatMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Chat message updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Chat message deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)   
class InternshipList(generics.ListCreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            internship = serializer.save()
            return Response({
                "message": "Internship created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class InternshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Internship updated successfully!",  
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Internship deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class InternshipSearch(generics.ListAPIView):
    serializer_class = InternshipSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return Internship.objects.filter(
                Q(title__icontains=query) | Q(company__name__icontains=query) | Q(location__icontains=query)
            )
        return Internship.objects.none()  # Return an empty queryset if no query is provided
class ScholarshipList(generics.ListCreateAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            scholarship = serializer.save()
            return Response({
                "message": "Scholarship created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ScholarshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Scholarship updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Scholarship deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class ScholarshipSearch(generics.ListAPIView):
    serializer_class = ScholarshipSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return Scholarship.objects.filter(
                Q(title__icontains=query) | Q(provider_name__icontains=query) | Q(description__icontains=query)
            )
        return Scholarship.objects.none()  # Return an empty queryset if no query is provided
class JobApplicationList(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            job_application = serializer.save()
            return Response({
                "message": "Job application created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class JobApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Job application updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Job application deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class InternshipApplicationList(generics.ListCreateAPIView):
    queryset = InternshipApplication.objects.all()
    serializer_class = InternshipApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            internship_application = serializer.save()
            return Response({
                "message": "Internship application created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class InternshipApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InternshipApplication.objects.all()
    serializer_class = InternshipApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Internship application updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Internship application deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)
class ScholarshipApplicationList(generics.ListCreateAPIView):
    queryset = ScholarshipApplication.objects.all()
    serializer_class = ScholarshipApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            scholarship_application = serializer.save()
            return Response({
                "message": "Scholarship application created successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ScholarshipApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScholarshipApplication.objects.all()
    serializer_class = ScholarshipApplicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Scholarship application updated successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            "message": "Scholarship application deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)

def job_posts(request):
    return render(request, 'base_template/job_post.html')
@login_required
def job_posts(request):
    # List all active job posts
    posts = JobPost.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'base_template/job_post.html', {'job_posts': posts})

@login_required
def create_job_post(request):
    if request.method == 'POST':
        try:
            # Get form data
            title = request.POST.get('title')
            company_name = request.POST.get('company_name')
            description = request.POST.get('description')
            requirements = request.POST.get('requirements')
            responsibilities = request.POST.get('responsibilities', '')
            required_skills = request.POST.get('required_skills')
            job_type = request.POST.get('job_type')
            experience_level = request.POST.get('experience_level')
            location = request.POST.get('location')
            is_remote = request.POST.get('is_remote') == 'on'
            salary_min = request.POST.get('salary_min')
            salary_max = request.POST.get('salary_max')
            currency = request.POST.get('currency', 'USD')
            application_deadline = request.POST.get('application_deadline')

            # Validate required fields
            if not all([title, company_name, description, requirements, 
                       required_skills, job_type, experience_level, location]):
                raise ValidationError("All required fields must be filled.")

            # Get or create company
            company, created = Company.objects.get_or_create(
                name=company_name,
                defaults={
                    'created_by': request.user,
                    'industry': 'Unknown',
                    'website': '',
                    'email': '',
                    'phone_number': '',
                }
            )

            # Parse application deadline if provided
            deadline = None
            if application_deadline:
                try:
                    deadline = datetime.datetime.strptime(application_deadline, '%Y-%m-%dT%H:%M')
                except ValueError:
                    raise ValidationError("Invalid date format for application deadline")

            # Create job post
            job_post = JobPost(
                title=title,
                company=company,
                description=description,
                requirements=requirements,
                responsibilities=responsibilities,
                job_type=job_type,
                experience_level=experience_level,
                location=location,
                is_remote=is_remote,
                salary_min=float(salary_min) if salary_min else None,
                salary_max=float(salary_max) if salary_max else None,
                currency=currency,
                application_deadline=deadline,
                posted_by=request.user,
                is_active=True
            )
            
            # Save the job post first to get an ID
            job_post.save()
            
            # Process skills (comma-separated list)
            skills_list = [skill.strip() for skill in required_skills.split(',') if skill.strip()]
            for skill_name in skills_list:
                skill, created = Skill.objects.get_or_create(name=skill_name)
                job_post.required_skills.add(skill)
            
            messages.success(request, 'Job post created successfully!')
            return redirect('job_posts')
            
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f'Error creating job post: {str(e)}')
    
    # For GET requests or if there's an error in POST, render the form
    return render(request, 'base_template/create_job_post.html')

@login_required
def view_job_post(request, post_id):
    try:
        job_post = JobPost.objects.get(id=post_id, is_active=True)
        # Increment view count
        job_post.views_count += 1
        job_post.save()
        return render(request, 'base_template/job_post_detail.html', {'job_post': job_post})
    except JobPost.DoesNotExist:
        messages.error(request, 'Job post not found or no longer available')
        return redirect('job_posts')

@login_required
def edit_job_post(request, post_id):
    try:
        job_post = JobPost.objects.get(id=post_id, posted_by=request.user)
        
        if request.method == 'POST':
            # Similar to create_job_post but with updates
            job_post.title = request.POST.get('title')
            company_name = request.POST.get('company_name')
            job_post.description = request.POST.get('description')
            job_post.requirements = request.POST.get('requirements')
            job_post.responsibilities = request.POST.get('responsibilities', '')
            required_skills = request.POST.get('required_skills')
            job_post.job_type = request.POST.get('job_type')
            job_post.experience_level = request.POST.get('experience_level')
            job_post.location = request.POST.get('location')
            job_post.is_remote = request.POST.get('is_remote') == 'on'
            job_post.salary_min = float(request.POST.get('salary_min')) if request.POST.get('salary_min') else None
            job_post.salary_max = float(request.POST.get('salary_max')) if request.POST.get('salary_max') else None
            job_post.currency = request.POST.get('currency', 'USD')
            
            if request.POST.get('application_deadline'):
                try:
                    job_post.application_deadline = datetime.datetime.strptime(
                        request.POST.get('application_deadline'), '%Y-%m-%dT%H:%M')
                except ValueError:
                    messages.error(request, "Invalid date format for application deadline")
                    return redirect('edit_job_post', post_id=post_id)
            
            # Update company if changed
            if job_post.company.name != company_name:
                company, created = Company.objects.get_or_create(
                    name=company_name,
                    defaults={
                        'created_by': request.user,
                        'industry': 'Unknown',
                        'website': '',
                        'email': '',
                        'phone_number': '',
                    }
                )
                job_post.company = company
            
            job_post.save()
            
            # Update skills
            job_post.required_skills.clear()
            skills_list = [skill.strip() for skill in required_skills.split(',') if skill.strip()]
            for skill_name in skills_list:
                skill, created = Skill.objects.get_or_create(name=skill_name)
                job_post.required_skills.add(skill)
            
            messages.success(request, 'Job post updated successfully!')
            return redirect('view_job_post', post_id=post_id)
        
        # For GET request, populate form with existing data
        skills = ", ".join([skill.name for skill in job_post.required_skills.all()])
        return render(request, 'base_template/edit_job_post.html', {
            'job_post': job_post,
            'skills': skills
        })
        
    except JobPost.DoesNotExist:
        messages.error(request, 'Job post not found or you are not authorized to edit it')
        return redirect('job_posts')

@login_required
def delete_job_post(request, post_id):
    try:
        job_post = JobPost.objects.get(id=post_id, posted_by=request.user)
        job_post.is_active = False
        job_post.save()
        messages.success(request, 'Job post has been deactivated')
    except JobPost.DoesNotExist:
        messages.error(request, 'Job post not found or you are not authorized to delete it')
    return redirect('job_posts')

def events(request):
    return render(request, 'opportunities/events.html')

def project_collab(request):
    return render(request, 'opportunities/project_collab.html')

def internships(request):
    return render(request, 'opportunities/internships.html')

def scholarships(request):
    return render(request, 'opportunities/scholarships.html')


















