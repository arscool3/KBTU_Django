from django.contrib import admin

from .models import Manager, Barber, Client, Barbershop, BookingRequest, ApplicationRequest

admin.site.register(Manager)
admin.site.register(Barber)
admin.site.register(Client)
admin.site.register(Barbershop)
admin.site.register(BookingRequest)
admin.site.register(ApplicationRequest)