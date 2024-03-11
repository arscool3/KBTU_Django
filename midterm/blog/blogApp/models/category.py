from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    
