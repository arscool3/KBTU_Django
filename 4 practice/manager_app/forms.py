from django import forms

from manager_app.models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class AuthorSelectionForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label=None, label="Select Author")

class TopicSelectionForm(forms.Form):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), empty_label=None, label='Select Topic')