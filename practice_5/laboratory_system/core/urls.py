from django.contrib import admin
from django.urls import path

# from core.views import add_book, add_student, add_teacher, add_admin

from core.views import *

urlpatterns = [
    path('book/', get_books),
    path('student/', get_student_by_name),
    path('teacher/',get_teacher ),
    path('add_book/', add_book, name='add_book'),
    path('add_student/', add_student, name='add_student'),
    path('add_teacher/', add_teacher, name='add_teacher'),
    path('add_admin/', add_admin, name='add_admin'),
    
]