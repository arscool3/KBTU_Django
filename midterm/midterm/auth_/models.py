from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    user = None
    email = models.EmailField(unique=True)


