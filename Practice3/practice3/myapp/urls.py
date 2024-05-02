from django.urls import path
from .views import create_item

urlpatterns = [
    path('', create_item, name='create_item'),
]
