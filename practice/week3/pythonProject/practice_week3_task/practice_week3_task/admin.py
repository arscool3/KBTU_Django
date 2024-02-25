from django.contrib import admin
from .models import MyModel


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')


admin.site.register(MyModel, MyModelAdmin)
