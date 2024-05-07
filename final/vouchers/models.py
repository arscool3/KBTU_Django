from django.db import models
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Voucher(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.CharField(max_length=300, default='')
    img = models.CharField(max_length=300, default='')
    like = models.IntegerField(default=0)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    username = models.CharField(max_length=300, default='Anonymous')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    def __str__(self):
            return f"{self.id} - {self.voucher}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.FloatField()

    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.voucher.name}"
