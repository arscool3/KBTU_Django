from django.urls import path
from .views import bookView, home


urlpatterns = [
    path('books/', bookView, name='books'),
    path('', home, name='home'),
]