from django import forms
from .models import Author,Book,Publisher,Magazine

class BookForm(forms.Form):
    name=forms.CharField(label="Book name", max_length=100)
    author=forms.ModelChoiceField(queryset=Author.objects.all())
    price=forms.IntegerField()
    def clean(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Price must be a positive number")
        return price    
class AuthorForm(forms.Form):
    name=forms.CharField(label="Author name", max_length=100)
class PublisherForm(forms.Form):
    name=forms.CharField(label="Publisher name", max_length=100)
class MagazineForm(forms.Form):
    name=forms.CharField(label="Magazine name", max_length=100)
    publisher=forms.ModelChoiceField(queryset=Publisher.objects.all())
    price=forms.IntegerField()
    def clean(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Price must be a positive number")
        return price          


