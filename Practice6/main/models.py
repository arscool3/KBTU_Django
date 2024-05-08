from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
from datetime import datetime, timedelta
from django.utils import timezone

class Days_of_Week(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=15)
    def __str__(self):
        return self.day

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
    airport_code = models.CharField(max_length=3,  validators=[MinLengthValidator(3)])
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
    flight_days = models.ManyToManyField(Days_of_Week)
    def __str__(self):
        return self.flight_code

    def generate_flights(self, period_type):
        data = Flight_dim.objects
        if period_type == 'month':
            last_date = data.filter(flight_code__flight_code = self.flight_code).order_by('-flight_date').first()

            if last_date:
                last_date = last_date.flight_date
            else:
                last_date = timezone.now().date()

            first_day_next_month = (last_date.replace(day=1) + timedelta(days=32)).replace(day=1)
            last_day_next_month = (first_day_next_month + timedelta(days=32)).replace(day=1) + timedelta(days=-1)

            next_month_dates = [first_day_next_month + timedelta(days=i) for i in range((last_day_next_month - first_day_next_month).days + 1)]

            flight_days_list = self.flight_days.values_list('id', flat=True)
            for date in next_month_dates:
                if date.weekday() + 1 in flight_days_list.all():
                    Flight_dim.objects.create(flight_code=self, flight_date=date, is_sale_open=False)



class FlightQuerySet(models.QuerySet):
    def get_flight_by_filter(self, airport_from: str, airport_to: str, flight_date: datetime):
        return self.filter(flight_code__airport_from__city=airport_from,flight_code__airport_to__city=airport_to, flight_date=flight_date)

class Flight_dim(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_code = models.ForeignKey(Flight_fact, on_delete=models.CASCADE)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=True)
    flight_date = models.DateField()
    is_sale_open = models.BooleanField()
    objects = FlightQuerySet.as_manager()

    def __str__(self):
        return self.flight_code.flight_code + ' (' + f'{self.flight_date}' + ')'

    def dept_date(self):
        return self.flight_date
