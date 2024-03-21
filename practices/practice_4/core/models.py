from django.db import models

from dataclasses import dataclass


class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Courier(Person):
    rating = models.FloatField()


class Order(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    delivery_date = models.DateField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='users')
    courier = models.ForeignKey('Courier', on_delete=models.CASCADE, related_name='couriers')


class User(Person):
    address = models.CharField(max_length=50)


# Relationships
# Courier <-> Order (One to Many)
# User <-> Order (One to Many)
