from django.contrib import admin

from core.models import *

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(OrderProduct)

admin.site.register(UserProfile)

admin.site.register(Cart)

admin.site.register(Review)
