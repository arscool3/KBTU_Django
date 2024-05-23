from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from doctors.models import Doctor
from patients.models import Patient
from rest_framework.exceptions import ValidationError

class UserRegistrationSerializer(serializers.ModelSerializer):
    ROLES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]

    role = serializers.ChoiceField(choices=ROLES, write_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'role']

    def validate_email(self, value):
        if Profile.objects.filter(email=value).exists():
            raise ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        role = validated_data.pop('role')
        profile = Profile.objects.create(**validated_data, is_doctor=(role == 'doctor'))
        if role == 'doctor':
            Doctor.objects.create(profile=profile)
        else:
            Patient.objects.create(profile=profile)

        return profile


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'