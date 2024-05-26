from django.db import models
from django import forms

class A1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

