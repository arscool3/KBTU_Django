# forms.py

from django import forms
from .models import Instructor, Member, Gym, Membership, Equipment, Workout

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['instructor_name', 'specialization', 'gender']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'age', 'membership_type', 'instructor']

class GymForm(forms.ModelForm):
    class Meta:
        model = Gym
        fields = ['gym_name', 'location', 'instructor']

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['name', 'price', 'member']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'quantity', 'gym']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'gym']

class InstructorFilterForm(forms.Form):
    specialization = forms.CharField(max_length=100, required=False)
    gender = forms.ChoiceField(choices=[('', 'Any'), ('Male', 'Male'), ('Female', 'Female')], required=False)

class GymFilterForm(forms.Form):
    location = forms.CharField(max_length=100, required=False)
