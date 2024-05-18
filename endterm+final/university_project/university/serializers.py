from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


# class CustomUserSerializer(serializers.ModelSerializer):
#     student = StudentSerializer(read_only=True)
#     professor = ProfessorSerializer(read_only=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'password', 'email', 'user_type', 'student', 'professor')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user_type = validated_data.pop('user_type')
#         user = CustomUser(**validated_data)
#         user.set_password(validated_data['password'])
#         user.user_type = user_type
#         user.save()
#         return user