from django.contrib import admin

from .models import Courier, User, Order

admin.site.register(Courier)
admin.site.register(User)
admin.site.register(Order)