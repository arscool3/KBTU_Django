from django.urls import path

from core.views import add_lesson, add_student, add_teacher

urlpatterns = [
    path('lesson/', add_lesson, name='add_lesson'),
    path('student/', add_student, name='add_student'),
    path('teacher/', add_teacher, name='add_teacher'),
]