from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(category__name = category_name) 
    
    def get_product_details(self, product_id):
        return self.get_queryset().filter(id = product_id)  
    
    
class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    
class CartManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    