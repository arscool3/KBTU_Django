# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
