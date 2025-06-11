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


# skillink/serializers.py

from rest_framework import serializers
from .models import Skill, UserJobSeeker, UserSkill
from .models import *
from django.contrib.auth.hashers import make_password, check_password # Ensure check_password is imported

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

    def validate_name(self, value):
        if Skill.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("A skill with this name already exists.")
        return value

class UserJobSeekerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    
    class Meta:
        model = UserJobSeeker
        fields = [
            'id', 'ujs_full_name', 'ujs_username', 'ujs_phone_number',
            'ujs_date_of_birth', 'ujs_email', 'password', 'ujs_address',
            'gender', 'areas_of_Interest' # Make sure areas_of_Interest is included if it's a field you want to register/update
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'ujs_email': {'required': True},
            'ujs_username': {'required': True}
        }

    def validate_ujs_email(self, value):
        if UserJobSeeker.objects.filter(ujs_email__iexact=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_ujs_username(self, value):
        if UserJobSeeker.objects.filter(ujs_username__iexact=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def create(self, validated_data):
        validated_data['ujs_password'] = make_password(validated_data.pop('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Handle password update separately
        if 'password' in validated_data:
            new_password = validated_data.pop('password')
           
            if not check_password(new_password, instance.ujs_password):
                instance.ujs_password = make_password(new_password)
            else:
          
                pass 
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

class UserSkillSerializer(serializers.ModelSerializer):
    skill_details = SkillSerializer(source='skill', read_only=True)
  
    user_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserSkill
        fields = [
            'id', 'ujs_full_name', 'skill', 'skill_details',
            'proficiency_level', 'years_of_experience', 'user_details'
        ]
        extra_kwargs = {
            'ujs_full_name': {'write_only': True}, # Make this write_only
            'skill': {'write_only': True}
        }

    def get_user_details(self, obj):
        # Ensure obj.ujs_full_name exists before accessing its attributes
        if obj.ujs_full_name:
            return {
                'id': obj.ujs_full_name.id,
                'username': obj.ujs_full_name.ujs_username,
                'full_name': obj.ujs_full_name.ujs_full_name
            }
        return None

    def validate(self, data):
        # Ensure both fields for unique_together are present for validation
        ujs_full_name_instance = data.get('ujs_full_name')
        skill_instance = data.get('skill')

        if ujs_full_name_instance and skill_instance and \
           UserSkill.objects.filter(ujs_full_name=ujs_full_name_instance, skill=skill_instance).exists():
            raise serializers.ValidationError("This user already has this skill.")
        return data

class UserJobSeekerDetailSerializer(UserJobSeekerSerializer):
    skills = UserSkillSerializer(many=True, read_only=True, source='skills')

    class Meta(UserJobSeekerSerializer.Meta):
        fields = UserJobSeekerSerializer.Meta.fields + ['skills']

# New: Login Serializer for handling authentication credentials
class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    def validate(self, data):
        username_or_email = data.get('username_or_email')
        password = data.get('password')

        if not username_or_email or not password:
            raise serializers.ValidationError("Both username/email and password are required.")

        user = None
        # Try to find user by username
        try:
            user = UserJobSeeker.objects.get(ujs_username__iexact=username_or_email)
        except UserJobSeeker.DoesNotExist:
            # If not found by username, try by email
            try:
                user = UserJobSeeker.objects.get(ujs_email__iexact=username_or_email)
            except UserJobSeeker.DoesNotExist:
                pass # User not found by either

        if user and user.check_password(password):
            # Store the authenticated user in context for the view to access
            self.context['user'] = user 
            return data
        else:
            raise serializers.ValidationError("Invalid credentials. Please check your username/email and password.")