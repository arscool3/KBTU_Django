from django import forms
from .models import Shop, Section, Producer, Goods

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ['name', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['name', 'description', 'price', 'quantity', 'stores', 'section', 'producer']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'stores': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'producer': forms.Select(attrs={'class': 'form-control'}),
        }