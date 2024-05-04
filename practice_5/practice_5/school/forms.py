from django import forms
from .models import Student, Teacher, Course, Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'enrollment_date']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'hire_date']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'date_joined']
