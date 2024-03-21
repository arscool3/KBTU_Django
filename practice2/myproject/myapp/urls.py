from django.urls import path
from .views import student_list_view

urlpatterns = [
    path('students/', student_list_view, name='student_list'),
]