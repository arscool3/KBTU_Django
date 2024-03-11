from django import forms
from blogApp.models.comment import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'text_comments'}
    
