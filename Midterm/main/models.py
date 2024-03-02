from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Aircraft():
    aircraft_id = models.AutoField(primary_key=True)
    aircraft_shortname = models.CharField(max_length=10)
    aircraft_builtyear = models.IntegerField(validators=[MaxValueValidator(int(datetime.date.today().year)), MinValueValidator(1900)])
    aircraft_capacity = models.IntegerField(validators=[MinValueValidator(1)])

class CustomerQuerySet(models.QuerySet):
    def filter_name_starting_with_D(self):
        return self.filter(name = r'K.*')

class City():
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    city_population = models.IntegerField(validators=[MinValueValidator(1)])

class Airport():
    airport_id = models.AutoField(primary_key=True)
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    airport_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    is_international = models.BooleanField()

class Airline():
    airline_id = models.AutoField(primary_key=True)
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)

class Item():
    item_id = models.IntegerField()
    cost = models.FloatField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Orders():
    order_id = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

#