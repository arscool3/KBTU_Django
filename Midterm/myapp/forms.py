from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'image', 'categories']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'text']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['post', 'author']


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['title', 'members']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['chat', 'sender', 'content']
