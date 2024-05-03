from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Request
from django import forms

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class RequestForm(forms.Form):
    class Meta:
        model = Request
        fields = ('title', 'description')

    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)
