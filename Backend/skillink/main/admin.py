from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

from .models import Skill, UserJobSeeker, UserSkill 
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