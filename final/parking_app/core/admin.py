from django.contrib import admin
from .models import DriverLicense, Car, ParkingLot, ParkingSpace, Payment

# Register your models here.

admin.site.register(DriverLicense)
admin.site.register(Car)
admin.site.register(ParkingLot)
admin.site.register(ParkingSpace)
admin.site.register(Payment)
