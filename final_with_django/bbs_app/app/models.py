from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username

class Barber(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    barbershop = models.ForeignKey('Barbershop', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Barbershop(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class Request(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('canceled', 'Canceled'),
        ('done', 'Done'),
    ]
    receiver = models.ForeignKey(Manager, related_name='received_%(class)ss', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class BookingRequest(Request):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    barbershop = models.ForeignKey(Barbershop, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.title = f"I want to book a seat in {self.barbershop} (Manager: {self.barbershop.manager})"
        super().save(*args, **kwargs)

class ApplicationRequest(Request):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    barbershop = models.ForeignKey(Barbershop, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.title = f"I want to work at {self.barbershop} (Manager: {self.barbershop.manager})"
        super().save(*args, **kwargs)
    