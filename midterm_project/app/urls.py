from django.contrib import admin
from django.urls import path

from .views import list_courses, course_detail, enrollment_form, create_course, create_lesson, take_quiz

urlpatterns = [
    path('courses/', list_courses, name='list_courses'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),
    path('courses/<int:course_id>/enroll/', enrollment_form, name='enrollment_form'),
    path('courses/create/', create_course, name='create_course'),
    path('courses/<int:course_id>/lessons/create/', create_lesson, name='create_lesson'),
    path('quizzes/<int:quiz_id>/', take_quiz, name='take_quiz'),
]
