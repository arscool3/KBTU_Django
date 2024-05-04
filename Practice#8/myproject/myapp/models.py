# models.py
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

