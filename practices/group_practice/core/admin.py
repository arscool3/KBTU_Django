from django.contrib import admin

from .models import Star, Planet, Satellite, Resident

admin.site.register(Star)
admin.site.register(Planet)
admin.site.register(Satellite)
admin.site.register(Resident)
