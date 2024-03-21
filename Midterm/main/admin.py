from django.contrib import admin
from .models import Airline, Aircraft, City, Airport, Flight_fact, Flight_dim, Days_of_Week

class FlightFactAdmin(admin.ModelAdmin):
    actions = ['generate_flights_for_next_month']

    def generate_flights_for_next_month(self, request, queryset):
        for flight in queryset:
            flight.generate_flights('month')
        self.message_user(request, "Flights generated successfully.")

admin.site.register(Airline)
admin.site.register(Aircraft)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Flight_fact, FlightFactAdmin)
admin.site.register(Flight_dim)
admin.site.register(Days_of_Week)