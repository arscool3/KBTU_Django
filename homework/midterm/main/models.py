from django.db import models
from users.models import User
# Create your models here.
class Basket(models.Model):
	user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

class Product(models.Model):
	title =models.CharField(max_length=30)
	price = models.PositiveIntegerField(default=0)
class In_Basket(models.Model):
	basket = models.ForeignKey(Basket,related_name="basket_of_user",on_delete=models.CASCADE)
	prodcut = models.ForeignKey(Product,related_name='product_of_user',on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
	user = models.ForeignKey(User,related_name="order_user",on_delete=models.CASCADE)
	data = models.DateField(auto_now=True)
	id = models.IntegerField(unique=True,primary_key=True)
class In_Order(models.Model):
	order = models.ForeignKey(Order,related_name="order_of_user",on_delete=models.CASCADE)
	prodcut = models.ForeignKey(Product,related_name='product_of_order',on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)