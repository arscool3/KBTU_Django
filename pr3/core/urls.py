from django.urls import path

from views import *

urlpatterns = [
    path('lesson/', add_lesson, name='add_lesson'),
    path('student/', add_student, name='add_student'),
    path('teacher/', add_teacher, name='add_teacher'),
]