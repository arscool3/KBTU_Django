from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    date = models.DateTimeField()

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=300)

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

class Sponsor(models.Model):
    name = models.CharField(max_length=300)
    event = models.ManyToManyField(Event)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='avatars/')
