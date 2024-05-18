from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    balance = models.FloatField()

class Manufacturer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    descr = models.CharField(max_length=2048)

class Entity(models.Model):
    name = models.CharField(max_length=128)
    descr = models.CharField(max_length=2048)
    class Meta:
        abstract: True
    def __str__(self):
        return self.name

class Category(Entity):
    pass

class Product(Entity):
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    cost = models.IntegerField()
    count = models.FloatField()

class HistoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(Customer, on_delete = models.CASCADE)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user+', '+self.product+':'+self.date

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(Customer, on_delete = models.CASCADE)
    text = models.CharField(max_length=2048)
    def __str__(self):
        return self.text[:50]