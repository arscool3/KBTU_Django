from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Resume(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(max_length=255)
    about = models.TextField()
    citizenship = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    salary = models.IntegerField()
    salary_type = models.CharField(max_length=255)
    main_language = models.CharField(max_length=255)
    skills = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='resume_city')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resume_user')
    citizenship_obj = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='resume_citizenship_obj')
    
    def __str__(self):
        return self.position

class Education(models.Model):
    level = models.CharField(max_length=255)
    university_name = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    end_date = models.DateField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education_resume')

class ForeignLanguage(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='foreign_languages_resume')

class EmploymentType(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class ResumeEmploymentType(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='employment_types_resume')
    employment_type = models.ForeignKey(EmploymentType, on_delete=models.CASCADE)

class WorkingHistory(models.Model):
    company_name = models.CharField(max_length=255)
    company_description = models.CharField(max_length=255)
    responsibilities = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='working_histories_resume')
