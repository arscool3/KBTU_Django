from django import forms

from main.models import Teacher, Student, Course, University


class TeacherForm(forms.ModelForm):
     class Meta:
        model = Teacher
        fields = '__all__'

class UniversityForm(forms.ModelForm):
     class Meta:
        model = University
        fields = '__all__'

class StudentForm(forms.ModelForm):
     class Meta:
        model = Student
        fields = '__all__'

class CourseForm(forms.ModelForm):
     class Meta:
        model = Course
        fields = '__all__'