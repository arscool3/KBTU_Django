from django.db import models
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Min

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255)
    photoUrl = models.TextField()

    def __str__(self):
        return f'Category name: {self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    photoUrl = models.TextField()

    def __str__(self):
        return f'Product name: {self.name}, category: {self.category} '




class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.FloatField()
   
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='carts')
    created_at = models.DateTimeField(default=datetime.now)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('product', 'cart')

class Store(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='stores')
    store_name = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.store_name}'



class StoreItem(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()