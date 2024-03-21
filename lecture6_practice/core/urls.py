from django.urls import path

from core.views import add_book, add_student, add_teacher, add_admin

urlpatterns = [
    path('book/', add_book, name='add_book'),
    path('student/', add_student, name='add_student'),
    path('teacher/', add_teacher, name='add_teacher'),
    path('admin/', add_admin, name='add_admin'),
]