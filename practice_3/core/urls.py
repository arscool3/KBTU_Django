from django.urls import path
from . import views

urlpatterns = [
    path("item/create/", views.item_create, name='item_create'),
    path("item/created/", views.item_created, name='item_created'),
]