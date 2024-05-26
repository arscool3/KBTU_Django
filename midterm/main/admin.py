from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(School)

admin.site.register(Course)

admin.site.register(Student)

admin.site.register(ContactInfo)

admin.site.register(Guardian)