from django.urls import path
from .views import WeatherDataAPIView

urlpatterns = [
    path('weather/<int:pk>/', WeatherDataAPIView.as_view(), name='weather-api'),
]

