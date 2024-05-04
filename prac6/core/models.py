# animal/models.py
from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
