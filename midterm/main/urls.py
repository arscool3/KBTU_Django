from django.urls import path

from .views import *

urlpatterns = [
    path('students',StudentListView.as_view(),),
    path('student/:id',StudentDetailView.as_view()),# перенаправляет на студента по аийдишке
    path('course',CourseListView.as_view()),
    path('course/:id',CourseDetailView.as_view()), # перенаправляет на курс по айди
    path('course/:id/students', CourseStudentsView.as_view()),
    path('contact',ContactInfoView.as_view())
]