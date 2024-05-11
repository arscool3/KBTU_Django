from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()


class Stock(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    area = models.IntegerField(help_text="Area in square meters")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    vendor = models.CharField(max_length=64)
    vendor_code = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return str(self.name) + " " + str(self.vendor_code)


class ProductsInStock(models.Model):
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.__str__() + " " + self.stock.__str__() + " " + str(self.quantity)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, editable=False)
    stock = models.ForeignKey(Stock, on_delete=models, editable=False)
    ordered_datetime = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.customer.__str__() + "'s order " + str(self.ordered_datetime)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, editable=False)
    quantity = models.IntegerField(editable=False)

    def __str__(self):
        return self.product.__str__() + " " + str(self.quantity)


class Delivery(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, editable=False)
    stock = models.ForeignKey(Stock, on_delete=models, editable=False)
    delivered_datetime = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.worker.__str__() + "'s delivery " + str(self.delivered_datetime)

class DeliveryLine(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, editable=False)
    quantity = models.IntegerField(editable=False)

    def __str__(self):
        return self.product.__str__() + " " + str(self.quantity)
