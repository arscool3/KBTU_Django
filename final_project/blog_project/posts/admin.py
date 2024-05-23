from django.contrib import admin
from .models import Category, Post

# Admin class for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

# Admin class for Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'category']
    search_fields = ['title', 'user__username', 'category__name']
    list_filter = ['created_at', 'category']
    readonly_fields = ['created_at']

# Registering the models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
