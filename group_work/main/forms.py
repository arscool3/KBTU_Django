from django import forms
from .models import Article, Destination

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = '__all__'

class DestinationForm(forms.ModelForm):
  class Meta:
    model = Destination
    fields = '__all__'