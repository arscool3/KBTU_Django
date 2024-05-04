from django.db import models
from django.contrib.auth.models import User



class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
 
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    date = models.DateField()




    def __str__(self):
        return self.title

class Schedule(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Schedule for {self.event.title}"


class Attendee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.IntegerField()
    

    def __str__(self):
        return f"{self.event.title} - {self.price}"

class Registration(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ticket}"