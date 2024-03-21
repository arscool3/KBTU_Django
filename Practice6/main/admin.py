from django.contrib import admin

from .models import Item, Seller, City, Customer

admin.site.register(Item)
admin.site.register(Seller)
admin.site.register(City)
admin.site.register(Customer)
