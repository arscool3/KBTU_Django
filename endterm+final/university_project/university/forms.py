from django import forms
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True})
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True})
        }


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
