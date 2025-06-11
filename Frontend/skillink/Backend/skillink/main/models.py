from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skills"

class UserJobSeeker(models.Model):
    ujs_full_name = models.CharField(max_length=30, blank=True, null=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    ujs_username = models.CharField(max_length=150, unique=True)
    ujs_phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    ujs_date_of_birth = models.DateField(blank=True, null=True)
    ujs_email = models.EmailField(unique=True)
    ujs_password = models.CharField(max_length=128) 
    ujs_address = models.CharField(max_length=100)    
    areas_of_Interest = models.TextField(blank=True, null=True)
    
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES, verbose_name="Gender",
        default='male')
    def save(self, *args, **kwargs):
        """Hashes password only if it's a new password or changed"""
        if self.pk:  # Check if instance exists (i.e., if it's an update)
            original = UserJobSeeker.objects.get(pk=self.pk)
            
            if original.ujs_password != self.ujs_password:
                self.ujs_password = make_password(self.ujs_password)  # Hash the new password if it’s changed
        else:  # New user
            self.ujs_password = make_password(self.ujs_password)  # Hash the password for a new user

        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Verify if raw_password matches the hashed password in DB"""
        return check_password(raw_password, self.ujs_password)  # Use your field name

    def verify_current_password(self, raw_password):
        """Alias for check_password (consistency with Django's naming)"""
        return self.check_password(raw_password)

    
    REQUIRED_FIELDS = ["ujs_username", "ujs_email", "ujs_password"]
    # def verify_password(self, raw_password):
    #     """Verifies the password without displaying it"""
    #     return check_password(raw_password, self.ujs_password)
    
    
    def __str__(self):
        return self.ujs_full_name

    class Meta:
        verbose_name_plural = "UserJobSeekers"
               
class UserSkill(models.Model):
    ujs_full_name = models.ForeignKey(UserJobSeeker, on_delete=models.CASCADE, related_name='skills')
    # user_id = models.IntegerField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_level = models.CharField(max_length=50, blank=True, null=True)
    years_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ujs_full_name} - {self.skill.name} ({self.proficiency_level})"
    
    class Meta:
        unique_together = ('ujs_full_name', 'skill') 
        verbose_name_plural = "User Skills"