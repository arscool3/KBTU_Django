from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
