from django.urls import path
from student import views

urlpatterns = [
    path('list/', views.index),
]
