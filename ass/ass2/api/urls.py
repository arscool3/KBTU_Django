from django.urls import path
from .views import list


urlpatterns = [
    path('students/', list, name='list'),
]