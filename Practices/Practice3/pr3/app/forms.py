from django import forms
from .models import *


class addPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
