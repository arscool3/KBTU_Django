from django.urls import path, include
from .views import *
urlpatterns = [
    path('getTime/', my_view)
]