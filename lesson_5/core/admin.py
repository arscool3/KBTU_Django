from django.contrib import admin

from core.models import Citizen, City, Country


admin.site.register(City)
admin.site.register(Country)
admin.site.register(Citizen)