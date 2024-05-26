from rest_framework import serializers
from .models import Student, Course, ContactInfo, Guardian, School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    contactinfo = ContactInfoSerializer(read_only=True)
    guardians = GuardianSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


# POST endpoints
        
