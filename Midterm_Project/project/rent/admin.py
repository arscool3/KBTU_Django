from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(User)