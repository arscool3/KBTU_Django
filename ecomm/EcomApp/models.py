from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class CustomManager(models.Manager):
    def mobile_list(self):
        return self.filter(category__iexact = "Mobile")
    
    def tv_list(self):
        return self.filter(category__iexact = "Tv")

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    prod_name = models.CharField(max_length = 30)
    type =[("mobile","Mobile"),("laptop","Laptop"),("Tv","TV")]
    category = models.CharField(max_length = 25,choices = type)
    desc =  models.CharField(max_length = 255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    objects = models.Manager()
    prod = CustomManager()

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, default = "", blank=True, null=True)

    def __str__(self):
        return f"{self.quantity}  {self.product.prod_name}"
    
class Order(models.Model):
    order_id = models.CharField(max_length = 50,default ="0")
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE, default = "", blank=True, null=True)
    is_completed = models.BooleanField(default =False)

class Address(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    address = models.CharField(max_length = 50)
    zipcode = models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    phone = models.BigIntegerField()

    def __str__(self) -> str:
        return self.address
