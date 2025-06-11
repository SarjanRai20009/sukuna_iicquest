from rest_framework import serializers
from .models import Skill, UserJobSeeker, UserSkill
from django.contrib.auth.hashers import make_password

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
            'gender'
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
       
        if 'password' in validated_data:
            validated_data['ujs_password'] = make_password(validated_data.pop('password'))
        return super().update(instance, validated_data)

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
            'ujs_full_name': {'write_only': True},
            'skill': {'write_only': True}
        }

    def get_user_details(self, obj):
       
        return {
            'id': obj.ujs_full_name.id,
            'username': obj.ujs_full_name.ujs_username,
            'full_name': obj.ujs_full_name.ujs_full_name
        }

    def validate(self, data):
      
        if UserSkill.objects.filter(
            ujs_full_name=data['ujs_full_name'],
            skill=data['skill']
        ).exists():
            raise serializers.ValidationError("This user already has this skill.")
        return data

# For nested representations (optional)
class UserJobSeekerDetailSerializer(UserJobSeekerSerializer):
    skills = UserSkillSerializer(many=True, read_only=True, source='skills')

    class Meta(UserJobSeekerSerializer.Meta):
        fields = UserJobSeekerSerializer.Meta.fields + ['skills']