from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/students', views.student),
    path('/teachers', views.teacher),
    path('/lessons', views.lesson),
    path('/faculties', views.faculty),
]