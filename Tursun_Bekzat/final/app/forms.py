from django import forms
from .models import Question, Answer, Tag
from django.contrib.auth.models import User


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'tags']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
