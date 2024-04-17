from django.contrib import admin
from django.urls import path

from views import *

urlpatterns = [
    path("", index, name='index'),
    path("main", main, name='main'),
    path("test", test, name='test')
]
