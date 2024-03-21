from django import forms
from .models import Paper, Tag, Category

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'abstract', 'authors', 'tags', 'category']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class TagSearchForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, label='Tags')

