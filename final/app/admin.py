from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Worker, Customer, Stock, Product, ProductsInStock, Order, Delivery


class WorkerInline(admin.StackedInline):
    model = Worker
    can_delete = False
    verbose_name_plural = "worker"


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = "customer"


class UserAdmin(BaseUserAdmin):
    inlines = [WorkerInline, CustomerInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(ProductsInStock)
admin.site.register(Order)
admin.site.register(Delivery)
