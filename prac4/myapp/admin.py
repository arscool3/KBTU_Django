from django.contrib import admin
from myapp.models import Product, Order, Category, Customer, Cart, CartItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)