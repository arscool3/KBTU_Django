
# Create your models here.
# models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    # Add more fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
