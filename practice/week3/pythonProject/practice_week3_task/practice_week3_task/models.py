from dataclasses import dataclass
import datetime
from django.db import models


# Relationship
# Student <-> Lesson (Many to many)
# Lesson <-> Teacher (Many to One)


class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.field1} {self.field2}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def expensive_products(self):
        return self.filter(price__gte=100)

class OrderManager(models.Manager):
    def high_value_orders(self):
        return self.filter(total_price__gte=500)