from django import forms
from .models import Student, Course, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
