from django.contrib import admin
from django.urls import path

from yourapp.views import index, test

urlpatterns = [
    path("", index, name='index'),
    # path("test/<int:id>", test, name='test')
]
