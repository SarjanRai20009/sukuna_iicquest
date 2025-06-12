from rest_framework import serializers
from .models import Skill, UserJobSeeker, UserSkill
from django.contrib.auth.hashers import make_password










# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = ['id', 'name', 'description']
#         read_only_fields = ['id']

#     def validate_name(self, value):
       
#         if Skill.objects.filter(name__iexact=value).exists():
#             raise serializers.ValidationError("A skill with this name already exists.")
#         return value

# class UserJobSeekerSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         write_only=True,
#         required=True,
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )
    
#     class Meta:
#         model = UserJobSeeker
#         fields = [
#             'id', 'ujs_full_name', 'ujs_username', 'ujs_phone_number',
#             'ujs_date_of_birth', 'ujs_email', 'password', 'ujs_address',
#             'gender'
#         ]
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'ujs_email': {'required': True},
#             'ujs_username': {'required': True}
#         }

#     def validate_ujs_email(self, value):
       
#         if UserJobSeeker.objects.filter(ujs_email__iexact=value).exists():
#             raise serializers.ValidationError("A user with this email already exists.")
#         return value

#     def validate_ujs_username(self, value):
       
#         if UserJobSeeker.objects.filter(ujs_username__iexact=value).exists():
#             raise serializers.ValidationError("A user with this username already exists.")
#         return value

#     def create(self, validated_data):
       
#         validated_data['ujs_password'] = make_password(validated_data.pop('password'))
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
       
#         if 'password' in validated_data:
#             validated_data['ujs_password'] = make_password(validated_data.pop('password'))
#         return super().update(instance, validated_data)

# class UserSkillSerializer(serializers.ModelSerializer):
#     skill_details = SkillSerializer(source='skill', read_only=True)
#     user_details = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = UserSkill
#         fields = [
#             'id', 'ujs_full_name', 'skill', 'skill_details',
#             'proficiency_level', 'years_of_experience', 'user_details'
#         ]
#         extra_kwargs = {
#             'ujs_full_name': {'write_only': True},
#             'skill': {'write_only': True}
#         }

#     def get_user_details(self, obj):
       
#         return {
#             'id': obj.ujs_full_name.id,
#             'username': obj.ujs_full_name.ujs_username,
#             'full_name': obj.ujs_full_name.ujs_full_name
#         }

#     def validate(self, data):
      
#         if UserSkill.objects.filter(
#             ujs_full_name=data['ujs_full_name'],
#             skill=data['skill']
#         ).exists():
#             raise serializers.ValidationError("This user already has this skill.")
#         return data

# # For nested representations (optional)
# class UserJobSeekerDetailSerializer(UserJobSeekerSerializer):
#     skills = UserSkillSerializer(many=True, read_only=True, source='skills')

#     class Meta(UserJobSeekerSerializer.Meta):
#         fields = UserJobSeekerSerializer.Meta.fields + ['skills']

# second

# from rest_framework import serializers
# from .models import Skill, UserJobSeeker, UserSkill
# from .models import *
# from django.contrib.auth.hashers import make_password, check_password # Ensure check_password is imported

# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = ['id', 'name', 'description']
#         read_only_fields = ['id']

#     def validate_name(self, value):
#         if Skill.objects.filter(name__iexact=value).exists():
#             raise serializers.ValidationError("A skill with this name already exists.")
#         return value

# class UserJobSeekerSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(

#         write_only=True,
#         required=True,
#         style={'input_type': 'password', 'placeholder': 'Password'}
#     )
    
#     class Meta:
#         model = UserJobSeeker
#         fields = [
#             'id', 'ujs_full_name', 'ujs_username', 'ujs_phone_number',
#             'ujs_date_of_birth', 'ujs_email', 'password', 'ujs_address',
#             'gender', 'areas_of_Interest' # Make sure areas_of_Interest is included if it's a field you want to register/update
#         ]
#         extra_kwargs = {
#             'password': {'write_only': True},
#             'ujs_email': {'required': True},
#             'ujs_username': {'required': True}
#         }

#     def validate_ujs_email(self, value):
#         if UserJobSeeker.objects.filter(ujs_email__iexact=value).exists():
#             raise serializers.ValidationError("A user with this email already exists.")
#         return value

#     def validate_ujs_username(self, value):
#         if UserJobSeeker.objects.filter(ujs_username__iexact=value).exists():
#             raise serializers.ValidationError("A user with this username already exists.")
#         return value

#     def create(self, validated_data):
#         validated_data['ujs_password'] = make_password(validated_data.pop('password'))
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         # Handle password update separately
#         if 'password' in validated_data:
#             new_password = validated_data.pop('password')
           
#             if not check_password(new_password, instance.ujs_password):
#                 instance.ujs_password = make_password(new_password)
#             else:
          
#                 pass 
        
#         # Update other fields
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
        
#         instance.save()
#         return instance

# class UserSkillSerializer(serializers.ModelSerializer):
#     skill_details = SkillSerializer(source='skill', read_only=True)
  
#     user_details = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = UserSkill
#         fields = [
#             'id', 'ujs_full_name', 'skill', 'skill_details',
#             'proficiency_level', 'years_of_experience', 'user_details'
#         ]
#         extra_kwargs = {
#             'ujs_full_name': {'write_only': True}, # Make this write_only
#             'skill': {'write_only': True}
#         }

#     def get_user_details(self, obj):
#         # Ensure obj.ujs_full_name exists before accessing its attributes
#         if obj.ujs_full_name:
#             return {
#                 'id': obj.ujs_full_name.id,
#                 'username': obj.ujs_full_name.ujs_username,
#                 'full_name': obj.ujs_full_name.ujs_full_name
#             }
#         return None

#     def validate(self, data):
#         # Ensure both fields for unique_together are present for validation
#         ujs_full_name_instance = data.get('ujs_full_name')
#         skill_instance = data.get('skill')

#         if ujs_full_name_instance and skill_instance and \
#            UserSkill.objects.filter(ujs_full_name=ujs_full_name_instance, skill=skill_instance).exists():
#             raise serializers.ValidationError("This user already has this skill.")
#         return data

# class UserJobSeekerDetailSerializer(UserJobSeekerSerializer):
#     skills = UserSkillSerializer(many=True, read_only=True, source='skills')

#     class Meta(UserJobSeekerSerializer.Meta):
#         fields = UserJobSeekerSerializer.Meta.fields + ['skills']

# # New: Login Serializer for handling authentication credentials
# class LoginSerializer(serializers.Serializer):
#     ujs_username = serializers.CharField(required=True)
#     password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

#     def validate(self, data):
#         ujs_username = data.get('ujs_username')
#         password = data.get('password')  # We accept 'password' from frontend

#         if not ujs_username or not password:
#             raise serializers.ValidationError("Both username and password are required.")

#         try:
#             user = UserJobSeeker.objects.get(ujs_username=ujs_username)
#             # check_password method compares raw password with hashed ujs_password
#             if user.check_password(password):
#                 self.context['user'] = user
#                 return data
#             else:
#                 raise serializers.ValidationError("Invalid password.")
#         except UserJobSeeker.DoesNotExist:
#             raise serializers.ValidationError("User with this username does not exist.")
# class PortfolioItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PortfolioItem
#         fields = [
#             'id', 'user', 'title', 'description', 'link', 'image', 'date_completed',
#             'created_at', 'updated_at'
#         ]
#         read_only_fields = ['id', 'user', 'created_at', 'updated_at'] # 'user' will be set by the view
from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']

class UserJobSeekerSerializer(serializers.ModelSerializer):
    portfolio_items = serializers.SerializerMethodField()
    skills_details = serializers.SerializerMethodField()
    full_name_with_username = serializers.SerializerMethodField()

    class Meta:
        model = UserJobSeeker
        fields = ['id', 'profile_image', 'ujs_full_name', 'ujs_username', 'ujs_phone_number', 
                  'ujs_date_of_birth', 'ujs_email', 'ujs_address', 'areas_of_Interest', 
                  'pan_number', 'gender', 'portfolio_items', 'skills_details', 'full_name_with_username']

    def get_portfolio_items(self, obj):
        items = obj.portfolio_items.all()
        return [{'title': item.title, 'description': item.description} for item in items]

    def get_skills_details(self, obj):
        skills = obj.skills.all()
        return [{'skill': user_skill.skill.name, 'proficiency': user_skill.proficiency_level} 
                for user_skill in skills]

    def get_full_name_with_username(self, obj):
        return f"{obj.ujs_full_name} (@{obj.ujs_username})"

    def validate_ujs_phone_number(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Phone number should be numeric and at least 10 digits long.")
        return value

class PortfolioItemSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioItem
        fields = ['id', 'user', 'user_details', 'title', 'description', 'link', 
                  'image', 'date_completed', 'created_at', 'updated_at']

    def get_user_details(self, obj):
        return {
            'name': obj.user.ujs_full_name,
            'email': obj.user.ujs_email
        }

class UserSkillSerializer(serializers.ModelSerializer):
    skill_name = serializers.SerializerMethodField()
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = UserSkill
        fields = ['id', 'ujs_full_name', 'user_details', 'skill', 'skill_name', 
                  'proficiency_level', 'years_of_experience']

    def get_skill_name(self, obj):
        return obj.skill.name

    def get_user_details(self, obj):
        return {
            'name': obj.ujs_full_name.ujs_full_name,
            'email': obj.ujs_full_name.ujs_email
        }

class CompanySerializer(serializers.ModelSerializer):
    job_posts_count = serializers.SerializerMethodField()
    news_events_count = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'website', 'email', 'phone_number', 
                  'address', 'logo', 'industry', 'company_size', 'founded_year', 
                  'is_verified', 'job_posts_count', 'news_events_count']

    def get_job_posts_count(self, obj):
        return obj.job_posts.count()

    def get_news_events_count(self, obj):
        return obj.news_events.count()

class MentorSerializer(serializers.ModelSerializer):
    specializations_list = serializers.SerializerMethodField()
    full_name_with_company = serializers.SerializerMethodField()

    class Meta:
        model = Mentor
        fields = ['id', 'full_name', 'email', 'phone_number', 'bio', 'profile_picture', 
                  'current_position', 'company', 'years_of_experience', 'specializations_list',
                  'linkedin_profile', 'hourly_rate', 'is_available', 'rating', 
                  'full_name_with_company']

    def get_specializations_list(self, obj):
        return [skill.name for skill in obj.specializations.all()]

    def get_full_name_with_company(self, obj):
        company_name = obj.company.name if obj.company else "Independent"
        return f"{obj.full_name} ({company_name})"

class ExpertSerializer(serializers.ModelSerializer):
    expertise_areas_list = serializers.SerializerMethodField()
    full_name_with_title = serializers.SerializerMethodField()

    class Meta:
        model = Expert
        fields = ['id', 'full_name', 'email', 'phone_number', 'bio', 'profile_picture',
                  'expertise_areas_list', 'current_position', 'company', 'years_of_experience',
                  'education', 'consultation_rate', 'is_available_for_consultation',
                  'rating', 'full_name_with_title']

    def get_expertise_areas_list(self, obj):
        return [skill.name for skill in obj.expertise_areas.all()]

    def get_full_name_with_title(self, obj):
        return f"{obj.full_name}, {obj.current_position}"

class JobPostSerializer(serializers.ModelSerializer):
    required_skills_list = serializers.SerializerMethodField()
    company_details = serializers.SerializerMethodField()
    days_remaining = serializers.SerializerMethodField()

    class Meta:
        model = JobPost
        fields = ['id', 'title', 'company', 'company_details', 'description', 'requirements',
                  'job_type', 'experience_level', 'location', 'is_remote', 'salary_min',
                  'salary_max', 'application_deadline', 'is_active', 'required_skills_list',
                  'days_remaining']

    def get_required_skills_list(self, obj):
        return [skill.name for skill in obj.required_skills.all()]

    def get_company_details(self, obj):
        return {
            'name': obj.company.name,
            'industry': obj.company.industry
        }

    def get_days_remaining(self, obj):
        if obj.application_deadline:
            from django.utils.timezone import now
            return (obj.application_deadline - now()).days
        return None

class NewsEventSerializer(serializers.ModelSerializer):
    tags_list = serializers.SerializerMethodField()
    company_details = serializers.SerializerMethodField()

    class Meta:
        model = NewsEvent
        fields = ['id', 'title', 'company', 'company_details', 'content', 'summary',
                  'event_type', 'featured_image', 'event_date', 'event_location',
                  'is_virtual', 'registration_url', 'tags_list', 'is_published']

    def get_tags_list(self, obj):
        return [skill.name for skill in obj.tags.all()]

    def get_company_details(self, obj):
        return {
            'name': obj.company.name,
            'logo': obj.company.logo.url if obj.company.logo else None
        }

class ChatRoomSerializer(serializers.ModelSerializer):
    participants_list = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'participants_list', 'mentor', 'expert',
                  'is_group_chat', 'last_message', 'created_at']

    def get_participants_list(self, obj):
        return [user.ujs_full_name for user in obj.participants.all()]

    def get_last_message(self, obj):
        last_msg = obj.messages.last()
        if last_msg:
            return {
                'message': last_msg.message[:50],
                'sender': last_msg.sender.ujs_full_name if last_msg.sender else (
                    last_msg.mentor_sender.full_name if last_msg.mentor_sender else last_msg.expert_sender.full_name
                ),
                'time': last_msg.created_at
            }
        return None

class ChatMessageSerializer(serializers.ModelSerializer):
    sender_info = serializers.SerializerMethodField()

    class Meta:
        model = ChatMessage
        fields = ['id', 'chat_room', 'sender', 'mentor_sender', 'expert_sender',
                  'sender_info', 'message', 'message_type', 'attachment',
                  'is_read', 'created_at']

    def get_sender_info(self, obj):
        if obj.sender:
            return {
                'type': 'user',
                'name': obj.sender.ujs_full_name,
                'image': obj.sender.profile_image.url if obj.sender.profile_image else None
            }
        elif obj.mentor_sender:
            return {
                'type': 'mentor',
                'name': obj.mentor_sender.full_name,
                'image': obj.mentor_sender.profile_picture.url if obj.mentor_sender.profile_picture else None
            }
        elif obj.expert_sender:
            return {
                'type': 'expert',
                'name': obj.expert_sender.full_name,
                'image': obj.expert_sender.profile_picture.url if obj.expert_sender.profile_picture else None
            }
        return None

class InternshipSerializer(serializers.ModelSerializer):
    required_skills_list = serializers.SerializerMethodField()
    company_details = serializers.SerializerMethodField()
    application_status = serializers.SerializerMethodField()

    class Meta:
        model = Internship
        fields = ['id', 'title', 'company', 'company_details', 'description',
                  'duration_months', 'start_date', 'end_date', 'location',
                  'is_remote', 'is_paid', 'stipend_amount', 'application_deadline',
                  'required_skills_list', 'application_status']

    def get_required_skills_list(self, obj):
        return [skill.name for skill in obj.required_skills.all()]

    def get_company_details(self, obj):
        return {
            'name': obj.company.name,
            'industry': obj.company.industry
        }

    def get_application_status(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if hasattr(request.user, 'userjobseeker'):
                return obj.applications.filter(applicant=request.user.userjobseeker).exists()
        return False

class ScholarshipSerializer(serializers.ModelSerializer):
    field_of_study_list = serializers.SerializerMethodField()
    application_status = serializers.SerializerMethodField()

    class Meta:
        model = Scholarship
        fields = ['id', 'title', 'provider', 'provider_name', 'description',
                  'amount', 'currency', 'scholarship_type', 'education_level',
                  'field_of_study_list', 'application_deadline', 'application_status']

    def get_field_of_study_list(self, obj):
        return [skill.name for skill in obj.field_of_study.all()]

    def get_application_status(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            if hasattr(request.user, 'userjobseeker'):
                return obj.applications.filter(applicant=request.user.userjobseeker).exists()
        return False

class JobApplicationSerializer(serializers.ModelSerializer):
    job_details = serializers.SerializerMethodField()
    applicant_details = serializers.SerializerMethodField()

    class Meta:
        model = JobApplication
        fields = ['id', 'job_post', 'job_details', 'applicant', 'applicant_details',
                  'cover_letter', 'status', 'applied_at']

    def get_job_details(self, obj):
        return {
            'title': obj.job_post.title,
            'company': obj.job_post.company.name
        }

    def get_applicant_details(self, obj):
        return {
            'name': obj.applicant.ujs_full_name,
            'email': obj.applicant.ujs_email
        }

class InternshipApplicationSerializer(serializers.ModelSerializer):
    internship_details = serializers.SerializerMethodField()
    applicant_details = serializers.SerializerMethodField()

    class Meta:
        model = InternshipApplication
        fields = ['id', 'internship', 'internship_details', 'applicant', 'applicant_details',
                  'cover_letter', 'portfolio_url', 'status', 'applied_at']

    def get_internship_details(self, obj):
        return {
            'title': obj.internship.title,
            'company': obj.internship.company.name
        }

    def get_applicant_details(self, obj):
        return {
            'name': obj.applicant.ujs_full_name,
            'email': obj.applicant.ujs_email
        }

class ScholarshipApplicationSerializer(serializers.ModelSerializer):
    scholarship_details = serializers.SerializerMethodField()
    applicant_details = serializers.SerializerMethodField()

    class Meta:
        model = ScholarshipApplication
        fields = ['id', 'scholarship', 'scholarship_details', 'applicant', 'applicant_details',
                  'personal_statement', 'status', 'applied_at']

    def get_scholarship_details(self, obj):
        return {
            'title': obj.scholarship.title,
            'provider': obj.scholarship.provider_name or (obj.scholarship.provider.name if obj.scholarship.provider else '')
        }

    def get_applicant_details(self, obj):
        return {
            'name': obj.applicant.ujs_full_name,
            'email': obj.applicant.ujs_email
        }