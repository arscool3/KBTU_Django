from rest_framework import serializers
from .models import Patient, PatientMedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.profile.first_name + " " + obj.profile.last_name
    
    class Meta:
        model = Patient
        fields = ['id', 'profile', 'full_name'] 

class PatientMedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedicalRecord
        fields = '__all__'
