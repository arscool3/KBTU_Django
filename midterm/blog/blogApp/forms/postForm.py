from django import forms
from blogApp.models.post import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'description', 'date', 'img'}