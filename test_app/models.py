from django.db import models

# Create your models here.
from django.db import models
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    roll_number = models.IntegerField()