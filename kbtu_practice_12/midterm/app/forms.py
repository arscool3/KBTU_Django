from django import forms
from .models import *

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class CityForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), to_field_name='name')
    class Meta:
        model = City
        fields = '__all__'

class ForeignLanguageForm(forms.ModelForm):
    class Meta:
        model = ForeignLanguage
        fields = '__all__'

class ResumeEmploymentTypeForm(forms.ModelForm):
    class Meta:
        model = ResumeEmploymentType
        fields = '__all__'

class WorkingHistoryForm(forms.ModelForm):
    class Meta:
        model = WorkingHistory
        fields = '__all__'

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

class EmploymentTypeForm(forms.ModelForm):
    class Meta:
        model = EmploymentType
        fields = '__all__'