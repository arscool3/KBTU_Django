from django.db import models
from .managers import First_Manager, Second_Manager

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    objects = Second_Manager()

    def __str__(self):
        return self.name


class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    objects = First_Manager()
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    objects = First_Manager()

    def __str__(self):
        return self.name




















































