from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User, Resume, Response


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'description', 'skills', 'experience']
        widgets = {'user': forms.HiddenInput()}
        labels = {'user': ''}
        required = {'user': False}

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['cover_letter']