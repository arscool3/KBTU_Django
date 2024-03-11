from django import forms
from blogApi.models.post import Post
from blogApi.models.category import Category

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ['title', 'description', 'date','category']
        