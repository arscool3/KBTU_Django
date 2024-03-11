from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=70)