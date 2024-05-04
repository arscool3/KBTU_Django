from django.contrib import admin
from .models import User, Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_active', 'category')
    list_filter = ('is_active', 'category')
    search_fields = ('title', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'user', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('content',)


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
