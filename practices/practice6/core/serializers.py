from core.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Org
        fields = '__all__'

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class CertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cert
        fields = '__all__'

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'