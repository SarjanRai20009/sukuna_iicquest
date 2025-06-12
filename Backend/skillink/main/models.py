from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    ujs_username = models.CharField(max_length=150, unique=True)
    ujs_phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    ujs_date_of_birth = models.DateField(blank=True, null=True)
    ujs_email = models.EmailField(unique=True)
    ujs_password = models.CharField(max_length=128) 
    ujs_address = models.CharField(max_length=100)    
    areas_of_Interest = models.TextField(blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True, unique=True)
    
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
class PortfolioItem(models.Model):
   
    user = models.ForeignKey(UserJobSeeker, on_delete=models.CASCADE, related_name='portfolio_items')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_completed', '-created_at'] # Order by most recent completion/creation date
        verbose_name_plural = "Portfolio Items"

    def __str__(self):
        return f"{self.user.ujs_full_name}'s Portfolio: {self.title}"
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


# Company Model
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    company_registration_certificate = models.FileField(upload_to='company_certificates/', blank=True, null=True)
    company_size = models.CharField(max_length=50, choices=[
        ('startup', 'Startup (1-10 employees)'),
        ('small', 'Small (11-50 employees)'),
        ('medium', 'Medium (51-200 employees)'),
        ('large', 'Large (201-1000 employees)'),
        ('enterprise', 'Enterprise (1000+ employees)'),
    ], blank=True, null=True)
    founded_year = models.IntegerField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


# Mentor Model
class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='mentor_profiles/', blank=True, null=True)
    current_position = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    years_of_experience = models.IntegerField()
    specializations = models.ManyToManyField(Skill, related_name='mentors')
    linkedin_profile = models.URLField(blank=True, null=True)
    github_profile = models.URLField(blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0,
                                validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    total_mentees = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.current_position}"

    class Meta:
        verbose_name_plural = "Mentors"


# Expert Model
class Expert(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='expert_profiles/', blank=True, null=True)
    expertise_areas = models.ManyToManyField(Skill, related_name='experts')
    current_position = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    years_of_experience = models.IntegerField()
    education = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    consultation_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_available_for_consultation = models.BooleanField(default=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0,
                                validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    total_consultations = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - Expert"

    class Meta:
        verbose_name_plural = "Experts"


# Job Post Model
class JobPost(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_posts')
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField(blank=True, null=True)
    required_skills = models.ManyToManyField(Skill, related_name='job_posts')
    job_type = models.CharField(max_length=50, choices=[
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ])
    experience_level = models.CharField(max_length=50, choices=[
        ('entry', 'Entry Level'),
        ('junior', 'Junior (1-3 years)'),
        ('mid', 'Mid Level (3-5 years)'),
        ('senior', 'Senior (5+ years)'),
        ('lead', 'Lead/Manager'),
    ])
    location = models.CharField(max_length=200)
    is_remote = models.BooleanField(default=False)
    salary_min = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    salary_max = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=3, default='USD')
    application_deadline = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    applications_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"

    class Meta:
        verbose_name_plural = "Job Posts"
        ordering = ['-created_at']


# News/Events Model
class NewsEvent(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='news_events')
    expert = models.ForeignKey(Expert, on_delete=models.SET_NULL, null=True, blank=True, related_name='news_events')
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True, related_name='news_events')
    content = models.TextField()
    summary = models.TextField(max_length=500, blank=True, null=True)
    event_type = models.CharField(max_length=50, choices=[
        ('news', 'Company News'),
        ('event', 'Event'),
        ('webinar', 'Webinar'),
        ('workshop', 'Workshop'),
        ('conference', 'Conference'),
        ('hackathon', 'Hackathon'),
        ('job_fair', 'Job Fair'),
    ])
    featured_image = models.ImageField(upload_to='news_events/', blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    event_location = models.CharField(max_length=200, blank=True, null=True)
    is_virtual = models.BooleanField(default=False)
    registration_url = models.URLField(blank=True, null=True)
    registration_deadline = models.DateTimeField(blank=True, null=True)
    max_participants = models.IntegerField(blank=True, null=True)
    current_participants = models.IntegerField(default=0)
    tags = models.ManyToManyField(Skill, related_name='news_events', blank=True)
    is_published = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.event_type}"

    class Meta:
        verbose_name_plural = "News & Events"
        ordering = ['-created_at']


# Chat Models
class ChatRoom(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    participants = models.ManyToManyField(UserJobSeeker, related_name='chat_rooms')
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True, related_name='chat_rooms')
    expert = models.ForeignKey(Expert, on_delete=models.SET_NULL, null=True, blank=True, related_name='chat_rooms')
    is_group_chat = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name:
            return self.name
        participants_names = ", ".join([p.ujs_full_name for p in self.participants.all()[:2]])
        return f"Chat: {participants_names}"

    class Meta:
        verbose_name_plural = "Chat Rooms"


class ChatMessage(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserJobSeeker, on_delete=models.CASCADE, related_name='sent_messages')
    mentor_sender = models.ForeignKey(Mentor, on_delete=models.CASCADE, null=True, blank=True, related_name='sent_messages')
    expert_sender = models.ForeignKey(Expert, on_delete=models.CASCADE, null=True, blank=True, related_name='sent_messages')
    message = models.TextField()
    message_type = models.CharField(max_length=20, choices=[
        ('text', 'Text'),
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ], default='text')
    attachment = models.FileField(upload_to='chat_attachments/', blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        sender_name = self.sender.ujs_full_name if self.sender else (
            self.mentor_sender.full_name if self.mentor_sender else self.expert_sender.full_name
        )
        return f"{sender_name}: {self.message[:50]}..."

    class Meta:
        verbose_name_plural = "Chat Messages"
        ordering = ['created_at']


# Internship Model
class Internship(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='internships')
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField(blank=True, null=True)
    required_skills = models.ManyToManyField(Skill, related_name='internships')
    duration_months = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    is_remote = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    stipend_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=3, default='USD')
    application_deadline = models.DateTimeField()
    max_applicants = models.IntegerField(blank=True, null=True)
    current_applicants = models.IntegerField(default=0)
    internship_type = models.CharField(max_length=50, choices=[
        ('summer', 'Summer Internship'),
        ('winter', 'Winter Internship'),
        ('part_time', 'Part-time Internship'),
        ('full_time', 'Full-time Internship'),
        ('research', 'Research Internship'),
    ])
    is_active = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"

    class Meta:
        verbose_name_plural = "Internships"
        ordering = ['-created_at']


# Scholarship Model
class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    provider = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='scholarships', blank=True, null=True)
    provider_name = models.CharField(max_length=200, help_text="If not a company, enter organization name")
    description = models.TextField()
    eligibility_criteria = models.TextField()
    required_documents = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    scholarship_type = models.CharField(max_length=50, choices=[
        ('merit', 'Merit-based'),
        ('need', 'Need-based'),
        ('research', 'Research'),
        ('minority', 'Minority'),
        ('field_specific', 'Field-specific'),
        ('international', 'International Students'),
    ])
    education_level = models.CharField(max_length=50, choices=[
        ('undergraduate', 'Undergraduate'),
        ('graduate', 'Graduate'),
        ('postgraduate', 'Postgraduate'),
        ('phd', 'PhD'),
        ('any', 'Any Level'),
    ])
    field_of_study = models.ManyToManyField(Skill, related_name='scholarships', blank=True)
    application_deadline = models.DateTimeField()
    start_date = models.DateField(blank=True, null=True)
    duration_years = models.IntegerField(blank=True, null=True)
    is_renewable = models.BooleanField(default=False)
    application_url = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    max_recipients = models.IntegerField(blank=True, null=True)
    current_applicants = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.provider_name}"

    class Meta:
        verbose_name_plural = "Scholarships"
        ordering = ['-created_at']


# Application Models for tracking user applications

class JobApplication(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(UserJobSeeker, on_delete=models.CASCADE, related_name='job_applications')
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('applied', 'Applied'),
        ('under_review', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ], default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.ujs_full_name} - {self.job_post.title}"

    class Meta:
        unique_together = ('job_post', 'applicant')
        verbose_name_plural = "Job Applications"


class InternshipApplication(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(UserJobSeeker, on_delete=models.CASCADE, related_name='internship_applications')
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('applied', 'Applied'),
        ('under_review', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ], default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.ujs_full_name} - {self.internship.title}"

    class Meta:
        unique_together = ('internship', 'applicant')
        verbose_name_plural = "Internship Applications"


class ScholarshipApplication(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(UserJobSeeker, on_delete=models.CASCADE, related_name='scholarship_applications')
    personal_statement = models.TextField()
    academic_transcripts = models.FileField(upload_to='transcripts/', blank=True, null=True)
    recommendation_letters = models.FileField(upload_to='recommendations/', blank=True, null=True)
    additional_documents = models.FileField(upload_to='scholarship_docs/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('applied', 'Applied'),
        ('under_review', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('awarded', 'Awarded'),
    ], default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.ujs_full_name} - {self.scholarship.title}"

    class Meta:
        unique_together = ('scholarship', 'applicant')
        verbose_name_plural = "Scholarship Applications"


class Content(models.Model):
    CONTENT_TYPES = [
        ('pdf', 'PDF Document'),
        ('video', 'Video'),
        ('docx', 'Word Document'),
        ('pptx', 'Presentation File'),
        ('url', 'External URL'),

    ]

    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    # Generic relation to either Expert, Mentor, or Company
    created_by_ct = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=models.Q(app_label='main', model__in=['expert', 'mentor', 'company'])
    )
    created_by_id = models.PositiveIntegerField()
    created_by = GenericForeignKey('created_by_ct', 'created_by_id')

    file = models.FileField(
        upload_to='content_files/',
        blank=True,
        null=True,
        help_text='Upload a file if content_type is pdf, video, or docx'
    )
    thumbnail = models.ImageField(
        upload_to='content_thumbnails/',
        blank=True,
        null=True,
        help_text='Thumbnail image (e.g. video preview or PDF cover)'
    )
    url = models.URLField(
        blank=True,
        null=True,
        help_text='Only required if content_type is url'
    )

    skills = models.ManyToManyField(Skill, related_name='contents', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_content_type_display()}) by {self.created_by}"

    class Meta:
        verbose_name_plural = "Contents"
        ordering = ['-created_at']
