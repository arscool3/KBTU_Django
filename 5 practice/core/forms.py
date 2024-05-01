from django import forms
from core.models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class StoryNoteForm(forms.ModelForm):
    class Meta:
        model = StoryNote
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class AuthorSelectionForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label=None, label="Select Author")

class PostSelectionForm(forms.Form):
    post = forms.ModelChoiceField(queryset=Post.objects.all(), empty_label=None, label='Select Post')