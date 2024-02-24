from django.contrib import admin

from core.models import Lesson, Teacher, Student

admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Student)