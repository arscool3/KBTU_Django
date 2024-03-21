from django.contrib import admin

from coursera.models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Review)
