from django.contrib import admin
from .models import Brand, Category, Product, Seller, Order, OrderItem

# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Order)
admin.site.register(OrderItem)