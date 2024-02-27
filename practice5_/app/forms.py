from django import forms
from .models import Corporation,Department,Employee,Project

class CorpForm(forms.Form):
    name = forms.CharField(label="Corporation name", max_length=100)
    field=forms.CharField(label="BusinessField", max_length=100)
    staff_number=forms.IntegerField(label="Staff Count")
class DepForm(forms.Form):
    name = forms.CharField(label="Department name", max_length=100)
    corporation = forms.ModelChoiceField(queryset=Corporation.objects.all())
    staff_number = forms.IntegerField()
    def clean_staff_number(self):
        staff_number = self.cleaned_data['staff_number']
        if staff_number < 0:
            raise forms.ValidationError("Staff number must be a positive number.")
        return staff_number
    

class EmpForm(forms.Form):
    name = forms.CharField(label="Employee name", max_length=100)
    position = forms.CharField(label="Position", max_length=100)
    salary = forms.IntegerField()
    age = forms.IntegerField()
    Depratment = forms.ModelChoiceField(queryset=Department.objects.all())
    def clean(self):
        cleaned_data = super().clean()
        salary = cleaned_data.get('salary')
        age = cleaned_data.get('age')

        if salary is not None and salary < 0:
            self.add_error('salary', "Salary must be a positive number.")

        if age is not None and age < 0:
            self.add_error('age', "Age must be a positive number.")

        return cleaned_data
 
class ProForm(forms.Form):
    name = forms.CharField(label="Project Name", max_length=100)
    budget=forms.IntegerField()
    is_successful=forms.BooleanField()
    employee=forms.ModelChoiceField(queryset=Employee.objects.all())
    def clean_budget(self):
        budget = self.cleaned_data['budget']
        if budget < 0:
            raise forms.ValidationError(" budget must be a positive number.")
        return budget
