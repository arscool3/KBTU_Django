from django import forms

from core.models import Student, Event, Organizer


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = '__all__'