from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    password = models.CharField(max_length=200)

