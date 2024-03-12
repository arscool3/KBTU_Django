from django.contrib import admin
from .models import Profile, Category, Comment, Like, Video
# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Video)


