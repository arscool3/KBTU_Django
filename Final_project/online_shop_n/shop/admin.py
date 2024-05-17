from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Review, Address

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(Address)