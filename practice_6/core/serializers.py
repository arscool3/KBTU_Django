from rest_framework import serializers
from core.models import *

class InstructorSerializer(serializers.Serializer):
    class Meta:
        model = Instructor
        fields = '__all__'


class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        fields = '__all__'
    
class AssignmentSerializer(serializers.Serializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class GradeSerializer(serializers.Serializer):
    class Meta:
        model = Grade
        fields = '__all__'

class AnnouncementsSerializer(serializers.Serializer):
    class Meta:
        model = Announcements
        fields = '__all__'