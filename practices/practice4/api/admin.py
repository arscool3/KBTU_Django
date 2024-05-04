from django.contrib import admin
from .models import School, Faculty, Course, Student

admin.site.register(School)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Student)
