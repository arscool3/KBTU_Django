from django.contrib import admin

from core.models import Country, City, Citizen, Car

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Citizen)
admin.site.register(Car)