from django import forms

class TaskForm(forms.Form):
    task_inp = forms.CharField(label='Task', max_length=100)
