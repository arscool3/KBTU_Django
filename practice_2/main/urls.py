from django.urls import path

from main.views import my_view

urlpatterns = [
    path('', my_view, name='my_view'),
]
