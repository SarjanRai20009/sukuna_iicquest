from django.urls import path
from . import views
from .views import *

from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from . import views # Correctly imports views from the same 'main' app folder

# Create a router and register our ViewSets with it.


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', SignIn, name = 'signin'),
    path('logout/', logout_view, name='logout'),

    path('opportunities/matching-jobs/', MatchingJobPostsView.as_view(), name='matching_jobs'),
    path('register/', views.register_user, name='register_user'),
    path('job_application/', views.job_posts, name='job_posts'),

    path('job-posts/', views.JobPostListView.as_view(), name='job_posts'),
    # path('viewcontents/', views.ContentListView.as_view(), name='ujs-content-list'),


    path('opportunities/events/', views.events, name='events'),
    path('opportunities/project_collab/', views.project_collab, name='project_collab'),
    path('opportunities/internships/', views.internships, name='internships'),
    path('opportunities/scholarships/', views.scholarships, name='scholarships'),
    
    path('skills/', views.SkillList.as_view(), name='api-skill-list'),
    path('skills/<int:pk>/', views.SkillDetail.as_view(), name='api-skill-detail'),
    path('skills/search/', views.SkillSearch.as_view(), name='api-skill-search'),
    # path('submit-job-post',views., name='submit_job_post'),
    # UserJobSeeker URLs
    path('user-job-seekers/', views.UserJobSeekerList.as_view(), name='api-user-job-seeker-list'),
    path('user-job-seekers/<int:id>/', views.UserJobSeekerDetail.as_view(), name='api-user-job-seeker-detail'), # Using 'id' as lookup_field

    # PortfolioItem URLs
    path('portfolio-items/', views.PortfolioItemList.as_view(), name='api-portfolio-item-list'),
    path('portfolio-items/<int:pk>/', views.PortfolioItemDetail.as_view(), name='api-portfolio-item-detail'),

    # UserSkill URLs
    path('user-skills/', views.UserSkillList.as_view(), name='api-user-skill-list'),
    path('user-skills/<int:pk>/', views.UserSkillDetail.as_view(), name='api-user-skill-detail'),

    # Company URLs
    path('companies/', views.CompanyList.as_view(), name='api-company-list'),
    path('companies/<int:id>/', views.CompanyDetail.as_view(), name='api-company-detail'), # Using 'id' as lookup_field
    path('companies/search/', views.CompanySearch.as_view(), name='api-company-search'),

    # Mentor URLs
    path('mentors/', views.MentorList.as_view(), name='api-mentor-list'),
    path('mentors/<int:id>/', views.MentorDetail.as_view(), name='api-mentor-detail'), # Using 'id' as lookup_field

    # Expert URLs
    path('experts/', views.ExpertList.as_view(), name='api-expert-list'),
    path('experts/<int:id>/', views.ExpertDetail.as_view(), name='api-expert-detail'), # Using 'id' as lookup_field

    # JobPost URLs
    path('job-posts/', views.JobPostList.as_view(), name='api-job-post-list'),
    path('job-posts/<int:id>/', views.JobPostDetail.as_view(), name='api-job-post-detail'), # Using 'id' as lookup_field
    path('job-posts/search/', views.JobPostSearch.as_view(), name='api-job-post-search'),

    # NewsEvent URLs
    path('news-events/', views.NewsEventList.as_view(), name='api-news-event-list'),
    path('news-events/<int:id>/', views.NewsEventDetail.as_view(), name='api-news-event-detail'), # Using 'id' as lookup_field
    path('news-events/search/', views.NewsEventSearch.as_view(), name='api-news-event-search'),

    # ChatRoom URLs
    path('chat-rooms/', views.ChatRoomList.as_view(), name='api-chat-room-list'),
    path('chat-rooms/<int:id>/', views.ChatRoomDetail.as_view(), name='api-chat-room-detail'), # Using 'id' as lookup_field

    # ChatMessage URLs
    path('chat-messages/', views.ChatMessageList.as_view(), name='api-chat-message-list'),
    path('chat-messages/<int:id>/', views.ChatMessageDetail.as_view(), name='api-chat-message-detail'), # Using 'id' as lookup_field

    # Internship URLs
    path('internships/', views.InternshipList.as_view(), name='api-internship-list'),
    path('internships/<int:id>/', views.InternshipDetail.as_view(), name='api-internship-detail'), # Using 'id' as lookup_field
    path('internships/search/', views.InternshipSearch.as_view(), name='api-internship-search'),

    # Scholarship URLs
    path('scholarships/', views.ScholarshipList.as_view(), name='api-scholarship-list'),
    path('scholarships/<int:id>/', views.ScholarshipDetail.as_view(), name='api-scholarship-detail'), # Using 'id' as lookup_field
    path('scholarships/search/', views.ScholarshipSearch.as_view(), name='api-scholarship-search'),

    # Application URLs
    path('job-applications/', views.JobApplicationList.as_view(), name='api-job-application-list'),
    path('job-applications/<int:id>/', views.JobApplicationDetail.as_view(), name='api-job-application-detail'),
    path('internship-applications/', views.InternshipApplicationList.as_view(), name='api-internship-application-list'),
    path('internship-applications/<int:id>/', views.InternshipApplicationDetail.as_view(), name='api-internship-application-detail'),
    path('scholarship-applications/', views.ScholarshipApplicationList.as_view(), name='api-scholarship-application-list'),
    path('scholarship-applications/<int:id>/', views.ScholarshipApplicationDetail.as_view(), name='api-scholarship-application-detail'),
  
]

