from django import forms
from blogApi.models.comments import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text_comments']