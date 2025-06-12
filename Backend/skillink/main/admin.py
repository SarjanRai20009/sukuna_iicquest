from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    
@admin.register(UserJobSeeker)    
class UserJobSeekerAdmin(admin.ModelAdmin):
    list_display = ('ujs_full_name', 'ujs_username', 'ujs_email', 'ujs_phone_number', 'ujs_date_of_birth', 'ujs_address', 'areas_of_Interest')
    search_fields = ('ujs_username', 'ujs_email', 'ujs_phone_number')
    list_filter = ('ujs_full_name','ujs_username' )
    ordering = ('ujs_username',)
    
@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('ujs_full_name', 'skill', 'proficiency_level', 'years_of_experience')  # Changed from user_job_seeker
    search_fields = ('ujs_full_name__ujs_username', 'skill__name')  # Updated to match the field name
    list_filter = ('proficiency_level', 'years_of_experience')
    ordering = ('ujs_full_name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'company_size', 'is_verified', 'created_at')
    search_fields = ('name', 'industry', 'email')
    list_filter = ('industry', 'company_size', 'is_verified', 'created_at')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'current_position', 'company', 'years_of_experience', 'rating', 'is_available')
    search_fields = ('full_name', 'email', 'current_position')
    list_filter = ('is_available', 'years_of_experience', 'company', 'created_at')
    filter_horizontal = ('specializations',)
    ordering = ('full_name',)
    readonly_fields = ('created_at', 'updated_at', 'total_mentees')


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'current_position', 'company', 'years_of_experience', 'rating', 'is_available_for_consultation')
    search_fields = ('full_name', 'email', 'current_position')
    list_filter = ('is_available_for_consultation', 'years_of_experience', 'company', 'created_at')
    filter_horizontal = ('expertise_areas',)
    ordering = ('full_name',)
    readonly_fields = ('created_at', 'updated_at', 'total_consultations')


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_type', 'experience_level', 'location', 'is_active', 'created_at')
    search_fields = ('title', 'company__name', 'location')
    list_filter = ('job_type', 'experience_level', 'is_remote', 'is_active', 'created_at')
    filter_horizontal = ('required_skills',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'views_count', 'applications_count')


@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'event_type', 'event_date', 'is_published', 'created_at')
    search_fields = ('title', 'company__name', 'content')
    list_filter = ('event_type', 'is_virtual', 'is_published', 'event_date', 'created_at')
    filter_horizontal = ('tags',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'views_count', 'current_participants')


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'expert', 'is_group_chat', 'is_active', 'created_at')
    search_fields = ('name', 'mentor__full_name', 'expert__full_name')
    list_filter = ('is_group_chat', 'is_active', 'created_at')
    filter_horizontal = ('participants',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('chat_room', 'sender', 'mentor_sender', 'expert_sender', 'message_type', 'is_read', 'created_at')
    search_fields = ('message', 'sender__ujs_full_name', 'mentor_sender__full_name', 'expert_sender__full_name')
    list_filter = ('message_type', 'is_read', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'duration_months', 'start_date', 'is_paid', 'is_active', 'created_at')
    search_fields = ('title', 'company__name', 'location')
    list_filter = ('is_remote', 'is_paid', 'internship_type', 'is_active', 'created_at')
    filter_horizontal = ('required_skills',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'views_count', 'current_applicants')


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider_name', 'amount', 'scholarship_type', 'education_level', 'is_active', 'created_at')
    search_fields = ('title', 'provider_name', 'description')
    list_filter = ('scholarship_type', 'education_level', 'is_renewable', 'is_active', 'created_at')
    filter_horizontal = ('field_of_study',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at', 'views_count', 'current_applicants')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job_post', 'status', 'applied_at')
    search_fields = ('applicant__ujs_full_name', 'job_post__title', 'job_post__company__name')
    list_filter = ('status', 'applied_at')
    ordering = ('-applied_at',)
    readonly_fields = ('applied_at', 'updated_at')


@admin.register(InternshipApplication)
class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'internship', 'status', 'applied_at')
    search_fields = ('applicant__ujs_full_name', 'internship__title', 'internship__company__name')
    list_filter = ('status', 'applied_at')
    ordering = ('-applied_at',)
    readonly_fields = ('applied_at', 'updated_at')


@admin.register(ScholarshipApplication)
class ScholarshipApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'scholarship', 'status', 'applied_at')
    search_fields = ('applicant__ujs_full_name', 'scholarship__title', 'scholarship__provider_name')
    list_filter = ('status', 'applied_at')
    ordering = ('-applied_at',)
    readonly_fields = ('applied_at', 'updated_at')
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'link', 'date_completed', 'created_at')
    search_fields = ('title', 'description', 'user__ujs_full_name', 'user__ujs_username')
    list_filter = ('date_completed', 'created_at')
    ordering = ('-date_completed', '-created_at') # Order by most recent completion/creation date
    readonly_fields = ('created_at', 'updated_at')