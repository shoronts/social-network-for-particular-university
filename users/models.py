from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User


class allUsersInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    current_date = models.DateTimeField(default=timezone.now)
    id_number = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    college = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    year_of_graduat = models.CharField(max_length=100, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class recomendationDetails(models.Model):

    current_date = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=500, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)

    user = models.CharField(max_length=100, blank=False, null=False)
    full_name = models.CharField(max_length=100, blank=False, null=False)
    university_of_graduation = models.CharField(max_length=100, blank=False, null=False)
    department_and_major = models.CharField(max_length=100, blank=False, null=False)
    graduations_degree = models.CharField(max_length=100, blank=False, null=False)
    grade_and_gpa = models.CharField(max_length=100, blank=False, null=False)
    studies_student_wishes_to_pursue = models.CharField(max_length=100, blank=False, null=False)
    specialization_in_higher_studies = models.CharField(max_length=100, blank=False, null=False)
    mobile_number = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)

    academic_excellence = models.CharField(max_length=100, blank=False, null=False)
    initiavive_and_motivation = models.CharField(max_length=100, blank=False, null=False)
    expreeing_ideas = models.CharField(max_length=100, blank=False, null=False)
    critical_thinking = models.CharField(max_length=100, blank=False, null=False)
    ability_to_accept_and_utilize_criticism = models.CharField(max_length=100, blank=False, null=False)
    self_confidence_and_responsibility = models.CharField(max_length=100, blank=False, null=False)
    ability_to_plan_and_execute_research = models.CharField(max_length=100, blank=False, null=False)
    acquiring_research_technique = models.CharField(max_length=100, blank=False, null=False)
    creative_and_originality = models.CharField(max_length=100, blank=False, null=False)
    linguistic_ikills = models.CharField(max_length=100, blank=False, null=False)
    general_knowledge = models.CharField(max_length=100, blank=False, null=False)
    overall_evaluation = models.CharField(max_length=100, blank=False, null=False)
    note_about_the_applicant = models.TextField(max_length=10000, blank=False, null=False)

    faculty_dean_name = models.CharField(max_length=100, blank=False, null=False)
    faculty_dean_signature = models.CharField(max_length=100, blank=False, null=False)
    faculty_dean_date = models.CharField(max_length=100, blank=False, null=False)

    recommenders_name = models.CharField(max_length=100, blank=False, null=False)
    academic_position = models.CharField(max_length=100, blank=False, null=False)
    academic_department = models.CharField(max_length=100, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.url)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/recommend-list/{self.slug}/'

    def __str__(self):
        return self.full_name
        