from rest_framework import serializers
from .models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['id', 'location', 'temperature', 'humidity', 'recorded_at']

