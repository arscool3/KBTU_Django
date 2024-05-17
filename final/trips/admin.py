from django.contrib import admin

from .models import Trip, Category, Comment, Favorite, Order, Profile

admin.site.register(Trip)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Order)
admin.site.register(Profile)

