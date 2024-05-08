from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class AddCourseForm(forms.Form):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), widget=forms.CheckboxSelectMultiple)


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        student = Student.objects.create(user=user)
        student.save()
        return user

class InstructorRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        instructor = Instructor.objects.create(user=user)
        instructor.save()
        return user
