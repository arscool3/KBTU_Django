from django.contrib import admin
from students.models import Student


@admin.register(Student)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'email', 'phone')
