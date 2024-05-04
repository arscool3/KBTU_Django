from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
class ShopQuerySet(models.QuerySet):
    def cities_shops(self, city_name: str):
        return self.filter(city=city_name)
    
    def shops_by_budget(self):
        return self.order_by("budget")

class Shop(Base):
    city = models.CharField(max_length=40)
    budget = models.FloatField(default=1000000000)
    objects = ShopQuerySet.as_manager()

class ProductQuerySet(models.QuerySet):
    def get_prods_by_category(self, category_name: str):
        return self.filter(category=category_name)
    
    def get_product(self, prod_id:str):
        return self.get(id=prod_id)
    
    def sort_by_price(self):
        return self.order_by("price")

class Product(Base):
    CATEGORY_CHOICES = (
        ("OTHER", "Other"),
        ("PHONES", "Phones"),
        ("LAPTOP", "Laptop"),
        ("TV", "tv"),
        ("APPLIANCES", "Appliances")
    )
    price = models.FloatField(default=10000)
    category = models.CharField(default = "Other", max_length=40, choices=CATEGORY_CHOICES)
    shop = models.ManyToManyField("Shop", related_name="shop")
    objects = ProductQuerySet.as_manager()



class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default="Pending")

class ReviewQuerySet(models.QuerySet):
    def listReviews(self, prod_id):
        return self.filter(product__id=prod_id)

class Review(Base):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default = 2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default = 2)
    rating = models.IntegerField()
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now())
    objects = ReviewQuerySet.as_manager()
