from django.contrib import admin
from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'code', 'dean')
    list_filter = ('dean',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    ordering = ('last_name', 'first_name')
    list_display = ('last_name', 'first_name', 'department', 'email', 'phone_number')
    list_filter = ('department',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name', 'code', 'department', 'professor', 'credits', 'is_active')
    list_filter = ('department', 'professor', 'is_active')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ordering = ('last_name', 'first_name')
    list_display = ('last_name', 'first_name', 'email', 'phone_number', 'address')
    list_filter = ('courses',)

#
# @admin.register(Schedule)
# class ScheduleAdmin(admin.ModelAdmin):
#     ordering = ('day_of_week', 'start_time')
#     list_display = ('course', 'day_of_week', 'start_time', 'end_time')
#
#
# @admin.register(Grade)
# class GradeAdmin(admin.ModelAdmin):
#     ordering = ('student', 'course')
#     list_display = ('student', 'course', 'grade', 'semester', 'academic_year')
#     list_filter = ('semester', 'academic_year')
