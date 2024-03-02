from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Airline(models.Model):
    airline_id = models.AutoField(primary_key=True)
    airline_name = models.CharField(max_length=50)
    airline_founded_date = models.DateField()

    def __str__(self):
        return self.airline_name

class Aircraft(models.Model):
    id = models.AutoField(primary_key=True)
    aircraft_code = models.CharField(max_length=10)
    full_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    built_date = models.DateField()
    full_capacity = models.IntegerField(validators=[MinValueValidator(1)])
    economy_capacity = models.IntegerField(validators=[MinValueValidator(0)])
    business_capacity = models.IntegerField(validators=[MinValueValidator(0)])
    owner_airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name + ' (' + self.aircraft_code + ')'

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city_population = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

class Airport(models.Model):
    airport_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    airport_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    is_international = models.BooleanField(choices=[
        (True, 'International'),
        (False, 'Domestic'),
    ])

    def __str__(self):
        return self.city.name + ' ' + self.airport_name
class Flight_fact(models.Model):
    flight_code = models.CharField(max_length=10)
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE)
    airport_from = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    airport_to = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')

    dept_time = models.TimeField()
    arr_time = models.TimeField()

    diff_days = models.IntegerField(validators=[MinValueValidator(-1), MaxValueValidator(1)])

    def __str__(self):
        return self.flight_code

class Flight_dim(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_code = models.ForeignKey(Flight_fact, on_delete=models.CASCADE)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    flight_date = models.DateField()
    is_sale_open = models.BooleanField()

    def __str__(self):
        return self.flight_code.flight_code + ' (' + f'{self.flight_date}' + ')'
