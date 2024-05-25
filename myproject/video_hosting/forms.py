from django import forms
from .models import Video, Comment

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'image', 'file', 'category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']