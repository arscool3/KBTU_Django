from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class addAdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['country', 'city', 'street', 'house', 'index']


class UserDescForm(forms.ModelForm):
    desc = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = UserInfo
        fields = ['desc']


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Юзернейм')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserImageForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ['photo']
