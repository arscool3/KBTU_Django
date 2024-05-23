from rest_framework import serializers
from .models import MedicalService, Specialty

class MedicalServiceSerializer(serializers.ModelSerializer):
    specialty_name = serializers.CharField(source='specialty.name', read_only=True)
    class Meta:
        model = MedicalService
        fields = ['id', 'name', 'specialty', 'specialty_name']

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
