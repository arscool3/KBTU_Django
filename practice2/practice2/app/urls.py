from django.urls import path
from .views import book_list_view

# Create your models here.
urlpatterns = [
    path('books/', book_list_view, name='student_list'),
]