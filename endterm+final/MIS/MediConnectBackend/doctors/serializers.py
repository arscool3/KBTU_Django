from rest_framework import serializers
from .models import Doctor, Appointment

class EnhancedDoctorSerializer(serializers.ModelSerializer):
    specialty_name = serializers.CharField(source='specialty.name', read_only=True)
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.profile.first_name + " " + obj.profile.last_name
    
    class Meta:
        model = Doctor
        fields = ['id', 'profile', 'full_name', 'specialty', 'specialty_name', 'clinic_location', 'iin_bin', 'license_number', 'license_issued_date', 'license_status'] 
    
    def update(self, instance, validated_data):
        instance.iin_bin = validated_data.get('iin_bin', instance.iin_bin)
        instance.license_number = validated_data.get('license_number', instance.license_number)
        instance.license_issued_date = validated_data.get('license_issued_date', instance.license_issued_date)
        instance.license_status = validated_data.get('license_status', instance.license_status)
        instance.save()
        return instance



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
