from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'travel_plan_app'

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Transportation(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    details = models.TextField()

class Accommodation(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    check_in = models.DateField()
    check_out = models.DateField()

class Activity(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
