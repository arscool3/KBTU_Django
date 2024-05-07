from django.contrib import admin

from .models import Voucher, Category, Comment, Favorite, Order

admin.site.register(Voucher)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Order)

