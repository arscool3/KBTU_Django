from django.db import models

class A1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()