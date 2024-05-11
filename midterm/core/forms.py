from django import forms
from .models import *

class GistForm(forms.ModelForm):
    class Meta:
        model = Gist
        fields = ["Name", "Description"]

class CommitForm(forms.ModelForm):
    class Meta:
        model = Commit
        fields = ["Comment"]

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["Name", "Code"]

