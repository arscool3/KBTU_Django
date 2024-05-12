from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Manager, Barber, Client, Barbershop, BookingRequest, ApplicationRequest
        
class ManagerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Manager
        fields = ['id', 'user', 'username', 'first_name', 'last_name']

class BarberSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Barber
        fields = ['id', 'user', 'username', 'barbershop']

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Client
        fields = ['id', 'user', 'username']

class BarbershopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbershop
        fields = ['id', 'name', 'manager']

class BookingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingRequest
        fields = ['id', 'receiver', 'status', 'timestamp', 'client', 'barbershop']

class ApplicationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationRequest
        fields = ['id', 'receiver', 'status', 'timestamp', 'barber', 'barbershop']
