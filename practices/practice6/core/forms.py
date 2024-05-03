from django import forms
from core.models import *

class LoginForm(forms.ModelForm):
    class Meta:
    	model = User
    	fields = [
            'username', 
            'password',
    	]

class UserForm(forms.ModelForm):
    class Meta:
    	model = User
    	fields = [
            'org',
            'username', 
            'password', 
            'email', 
            'first_name', 
            'last_name'
    	]

class OrgForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = '__all__'

class CourseForm(forms.Form):
    title = forms.CharField(max_length=30)
    descr = forms.CharField(max_length=255)
    cert_title = forms.CharField(max_length=30)
    cert_descr = forms.CharField(max_length=255)

class LessonForm(forms.ModelForm):
    class Meta:
    	model = Lesson
    	fields = [
            'course', 
    	]
    title = forms.CharField(max_length=30)
    text = forms.CharField(max_length=5000)
    quiz_title = forms.CharField(max_length=30)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'correct', 
            'answer0', 
            'answer1', 
            'answer2', 
            'answer3'
    	]