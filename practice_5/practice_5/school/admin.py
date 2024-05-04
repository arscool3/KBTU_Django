from django.contrib import admin
from .models import Student, Teacher, Course, Enrollment


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment_date')
    search_fields = ('first_name', 'last_name')
    list_filter = ('enrollment_date',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'hire_date')
    search_fields = ('first_name', 'last_name')
    list_filter = ('hire_date',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    list_filter = ('teacher',)
    search_fields = ('name',)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ('student__first_name', 'course__name')


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
