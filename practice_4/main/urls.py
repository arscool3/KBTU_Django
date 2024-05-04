from django.contrib import admin
from django.urls import path, include
from main.views import get_dorms, get_budget, get_gpa, get_language, get_univesities, add_course, add_university, add_student, add_teacher

urlpatterns = [
    path('university', add_university, name='add_university'),
    path('course/', add_course, name='add_course'),
    path('student/', add_student, name='add_student'),
    path('teacher/', add_teacher, name='add_teacher'),
    path('budget', get_budget),
    path('languages', get_language),
    path('stud_gpa', get_gpa),
    path('stud_dorm', get_dorms)
]
