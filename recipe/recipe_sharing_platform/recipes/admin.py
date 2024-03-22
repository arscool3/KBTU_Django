from django.contrib import admin
from .models import Category, Ingredient, Recipe, Rating, Comment

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(Comment)
