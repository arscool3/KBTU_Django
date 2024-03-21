from django.contrib import admin
from django.urls import path

from hello.views import index, test

urlpatterns = [
    path('', index, name='index'),
    path('test/<int:id>', test, name='test')
]