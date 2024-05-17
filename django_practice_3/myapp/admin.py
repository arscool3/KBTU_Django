from django.contrib import admin

from myapp.models import Lesson, Teacher, Student

admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Student)