from django import forms
from .models import Lesson, Course


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
