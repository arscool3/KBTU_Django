from django.contrib.auth.models import AbstractUser
from django.db import models

    
class CustomUser(AbstractUser):
    user = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


