from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Resume, Response

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'description', 'skills', 'experience']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['cover_letter']
