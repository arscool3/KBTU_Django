from django import forms

from .models import *


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandChooseForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), empty_label=None, label="choose brand")


class ResellerForm(forms.ModelForm):
    class Meta:
        model = Reseller
        fields = '__all__'


class ResellerChooseForm(forms.Form):
    reseller = forms.ModelChoiceField(queryset=Reseller.objects.all(), empty_label=None, label='choose reseller')


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'


class ShowroomForm(forms.ModelForm):
    class Meta:
        model = Showroom
        fields = '__all__'