from django.contrib import admin
from .models import Category, Product, CartItem, Cart, Seller, SellerItem
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (  'product','quantity', 'cart' )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (  'user','created_at' )

@admin.register(Seller)
class CartAdmin(admin.ModelAdmin):
    list_display = (  'user','seller_name' )

@admin.register(SellerItem)
class CartAdmin(admin.ModelAdmin):
    list_display = (  'seller','product','quantity','price')