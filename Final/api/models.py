from django.contrib.auth.models import PermissionsMixin, AbstractUser, User
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    small_descr = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    photo = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=30)
    photo = models.TextField()
    products = models.ManyToManyField(Product)  # Вместо форейгн кей


class Manager(models.Model):
    username = models.CharField(max_length=30)
    age = models.IntegerField(blank=True)
    password = models.TextField()
    is_admin = models.BooleanField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

