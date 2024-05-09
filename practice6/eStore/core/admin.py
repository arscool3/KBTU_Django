from django.contrib import admin
from .models import Category, Product,CartItem,Cart,Store, StoreItem
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

@admin.register(Store)
class CartAdmin(admin.ModelAdmin):
    list_display = (  'user','store_name' )

@admin.register(StoreItem)
class CartAdmin(admin.ModelAdmin):
    list_display = (  'store','product','quantity','price')