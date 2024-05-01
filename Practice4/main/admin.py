from django.contrib import admin
from .models import Client, Manager, Request

admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(Request)
