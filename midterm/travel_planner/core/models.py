from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)

class Ticket(models.Model):
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Flight from {self.departure_city} to {self.destination_city}, Flight Number: {self.flight_number}"

class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    destination_city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tour(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

