from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=250)
    image = models.TextField(null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField()
    location = models.ForeignKey('Location', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text


class Request(models.Model):
    phone = models.TextField()
    email = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.PROTECT, null=True)
    tour = models.ForeignKey('Tour', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Booking(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    tour = models.ForeignKey('Tour', on_delete=models.PROTECT, null=True)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.tour.name} by {self.user.username}"


class Rating(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.user.username} rated {self.tour.name} {self.rating} stars"
