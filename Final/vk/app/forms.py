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


class addCommentForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Comment
        fields = ['text']


class PostForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Post
        fields = ['text']


class ImageForm(forms.ModelForm):
    photo = forms.ImageField()

    class Meta:
        model = Image
        fields = ['photo']

