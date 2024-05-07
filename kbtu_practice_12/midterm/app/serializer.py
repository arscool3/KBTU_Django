from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['first_name', 'last_name', 'phone', 'birthday', 'gender', 'about', 'citizenship',
                  'position', 'salary', 'salary_type', 'main_language', 'skills', 'city', 'user', 'citizenship_obj']
