from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('destinations/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    path('trips/create/', views.create_trip, name='create_trip'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('user/trips/', views.user_trips, name='user_trips'),
    # Additional URLs for other endpoints...
]
