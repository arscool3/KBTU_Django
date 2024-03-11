from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Add other fields as needed
        widgets = {
            'password': forms.PasswordInput(),
        }

class SuperuserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user