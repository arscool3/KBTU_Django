from django.urls import path
from .views import createbook

urlpatterns = [
    path('createbook/', createbook, name='createbook'),
]