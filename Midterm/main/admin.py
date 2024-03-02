from django.contrib import admin

from .models import Airline, Aircraft, City, Airport, Flight_fact, Flight_dim

admin.site.register(Airline)
admin.site.register(Aircraft)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Flight_fact)
admin.site.register(Flight_dim)
