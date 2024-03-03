from django.contrib import admin
from django.urls import path
from core.views import add_product

urlpatterns = [
    path('', add_product)
]
