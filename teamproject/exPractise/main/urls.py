from django.urls import path
from .views import *
urlpatterns = [
    path('book/',get_book),
    path('reviews/',get_reviews)
]
