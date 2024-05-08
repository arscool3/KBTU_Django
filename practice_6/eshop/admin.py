from django.contrib import admin
from .models import Category, Product, UserProfile, Order, Cart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
