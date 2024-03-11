from django.db import models
from auth_.models import CustomUser
from .managers import ProductManager, CategoryManager

class Category(models.Model):
    name = models.CharField(max_length=100)
    objects = CategoryManager()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    objects = ProductManager()

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    products = models.ManyToManyField(Product)
    total_price = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.IntegerField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.user.username

