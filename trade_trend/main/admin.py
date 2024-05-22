from django.contrib import admin
from main.models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Notification)