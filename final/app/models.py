from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.user.__str__()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.user.__str__()


class Stock(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    area = models.IntegerField(help_text="Area in square meters")

    objects = models.Manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    vendor = models.CharField(max_length=64)
    vendor_code = models.CharField(max_length=16, unique=True)
    stock = models.ManyToManyField(Stock, through='ProductsInStock')

    objects = models.Manager()

    def __str__(self):
        return str(self.name) + " " + str(self.vendor_code)


class ProductsInStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('stock', 'product')

    objects = models.Manager()

    def __str__(self):
        return self.product.__str__() + " " + self.stock.__str__() + " " + str(self.quantity)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ordered_datetime = models.DateTimeField(auto_now_add=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.customer.__str__() + "'s order " + str(self.ordered_datetime)


class Delivery(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    delivered_datetime = models.DateTimeField(auto_now_add=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.worker.__str__() + "'s delivery " + str(self.delivered_datetime)
