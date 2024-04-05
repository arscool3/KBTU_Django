from django.contrib import admin

from .models import UserProfile, Course, Lesson, Enrollment, Instructor, Quiz

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Quiz)