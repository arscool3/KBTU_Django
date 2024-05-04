from django import forms

from main.models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'