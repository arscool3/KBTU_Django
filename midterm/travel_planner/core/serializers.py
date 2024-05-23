from .models import Ticket, Accommodation, Place

from rest_framework import serializers

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name']

class TicketSerializer(serializers.ModelSerializer):
    available_cities = Place.objects.values_list('name', flat=True)

    departure_city = serializers.ChoiceField(choices=available_cities)
    destination_city = serializers.ChoiceField(choices=available_cities)
    class Meta:
        model = Ticket
        fields = ['id', 'flight_number', 'price', 'departure_city', 'destination_city', 'date']

    def validate(self, data):
        if data['departure_city'] == data['destination_city']:
            raise serializers.ValidationError("Departure city and destination city cannot be the same.")
        return data

class AccommodationSerializer(serializers.ModelSerializer):
    available_cities = Place.objects.values_list('name', flat=True)
    destination_city = serializers.ChoiceField(choices=available_cities)

    class Meta:
        model = Accommodation
        fields = ['id', 'name', 'price_per_night', 'destination_city']
