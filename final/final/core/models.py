from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='customer')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/customers/',blank=True)

class Manufacturer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='manufacturer')
    descr = models.TextField()
    image = models.ImageField(upload_to='images/manufacturers/',blank=True)

class Entity(models.Model):
    name = models.CharField(max_length=128,db_index=True)
    descr = models.TextField()
    class Meta:
        abstract = True
    def __str__(self):
        return self.name

class Category(Entity):
    class Meta:
        verbose_name_plural = 'Categories'

class Product(Entity):
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='products')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    image = models.ImageField(upload_to='images/products/',blank=True)

class HistoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name='history')
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.date}, {self.user}: {self.product}"

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='comments')
    user = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name='comments')
    text = models.TextField()
    def __str__(self):
        return self.text[:50]