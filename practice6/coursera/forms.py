from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from coursera.models import *


class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(StudentRegistrationForm, self).save(commit=False)
        if commit:
            user.save()
            student = Student.objects.create(user=user)
        return user


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
