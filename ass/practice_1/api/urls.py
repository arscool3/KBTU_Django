from django.urls import path
from .views import hello_world, home, about



urlpatterns = [
    path('helloworld/', hello_world, name='event_list'),
    path('home/', home, name='event_list'),
    path('about/', about, name='event_list'),
]