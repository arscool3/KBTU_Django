from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'image')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('author', 'created_at', 'categories')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'timestamp')
    search_fields = ('post__title', 'author__username')
    list_filter = ('post', 'author', 'timestamp')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'author')
    search_fields = ('post__title', 'author__username')
    list_filter = ('post', 'author')


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    filter_horizontal = ('members',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sender', 'timestamp')
    search_fields = ('chat__title', 'sender__username')
    list_filter = ('chat', 'sender', 'timestamp')
