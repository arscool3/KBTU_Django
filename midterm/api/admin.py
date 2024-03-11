from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')


@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    list_display = ('id', 'sort')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'sort')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating')


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'text')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user',)