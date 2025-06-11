from django.urls import path
from . import views
from .views import *

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from . import views # Correctly imports views from the same 'main' app folder

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'skills', views.SkillViewSet)
router.register(r'users', views.UserJobSeekerViewSet, basename='user') 
router.register(r'user-skills', views.UserSkillViewSet)


urlpatterns = [
    # --- Authentication API Endpoints (from APIView) ---
    # path('register/', views.RegisterUserJobSeekerAPIView.as_view(), name='api_register'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', views.LogoutAPIView.as_view(), name='api_logout'),

    # --- Router generated API Endpoints ---
    # These will be prefixed by 'api/' from the project's root urls.py
    path('', include(router.urls)), # This line includes all ViewSet URLs
]

