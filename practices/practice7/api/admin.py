from django.contrib import admin

from .models import Subscriber, BlogPost

admin.site.register(Subscriber)
admin.site.register(BlogPost)