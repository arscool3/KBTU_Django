from django.urls import path
from .views import my_view

urlpatterns = [
    path('my-view/', my_view, name='my-view'),
]
