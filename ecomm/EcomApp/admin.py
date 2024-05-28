from django.contrib import admin
from . models import Product,CartItem,Order,Address

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)

class OrderAdmin(admin.ModelAdmin):
    list_display = ["product_id","quantity","user","is_completed"]
admin.site.register(Order,OrderAdmin)

admin.site.register(Address)