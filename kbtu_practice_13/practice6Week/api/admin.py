from django.contrib import admin
from .models import *
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'time')  # Display these fields in the list view
    search_fields = ['name']

admin.site.register(MyModel)