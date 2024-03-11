from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField()
    description = models.TextField()