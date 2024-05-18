from django import forms

from .models import *


class FitnessUserForm(forms.ModelForm):
    class Meta:
        model = FitnessUser
        exclude = ['user']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['user']


class DietForm(forms.ModelForm):
    class Meta:
        model = Diet
        exclude = ['user', 'registered_datetime']


class HealthMetricsForm(forms.ModelForm):
    class Meta:
        model = HealthMetrics
        exclude = ['user']


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = ['user']


class ProgressForm(forms.ModelForm):
    class Meta:
        model = CurrentProgress
        exclude = ['user', 'burnt_calories', 'eaten_calories']
