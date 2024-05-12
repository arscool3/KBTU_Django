from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User, Resume, Response, Skill, Vacancy


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        required = {'first_name': True, 'last_name': True}


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


class VacancyFilterForm(forms.Form):
    skills = forms.CharField(label='Skills', required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter skills, separated by commas'}))

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'salary_min', 'salary_max', 'skills', 'company', 'is_active']


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
