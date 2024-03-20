from django.db import models
from .managers import ProductManager, CategoryManager

class Category(models.Model):
    name = models.CharField(max_length=100)
    objects = CategoryManager()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    objects = ProductManager()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order for {self.product.name}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.name
