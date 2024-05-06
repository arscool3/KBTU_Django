from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    email = models.CharField(max_length=255, blank=True, null=False, unique=True)
    password = models.CharField(max_length=255, blank=True, null=False)
    is_doctor = models.BooleanField(default=False)
    