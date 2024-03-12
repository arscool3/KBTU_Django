from django.db import models

class MyModel(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.TextField()
    IDStudent = models.IntegerField()