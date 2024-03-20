from django.contrib import admin
from myapp.models import Category, Product, Order, Customer

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)