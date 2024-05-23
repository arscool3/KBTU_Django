from django.contrib import admin
from .models import User, Post, Comment, Like, Follow, UserProfile, CeleryTask

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(UserProfile)
admin.site.register(CeleryTask)
