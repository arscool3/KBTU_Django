from django import forms
from .models import Manager, Department, Employee, Project

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'manager']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'department']
