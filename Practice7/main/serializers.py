from rest_framework import serializers
from .models import Flight_dim, Aircraft

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ('full_name',)  # Include other fields as needed

class FlightDimSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer()

    class Meta:
        model = Flight_dim
        fields = ('flight_id', 'aircraft')  # Include other fields from Flight_dim as needed
