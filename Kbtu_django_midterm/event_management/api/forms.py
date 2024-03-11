from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Organizer, Event, Ticket, Schedule, Registration, Attendee

class OrganizerSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            organizer = Organizer.objects.create(user=user, name=self.cleaned_data['name'])
            organizer.save()
        return user


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['attendee', 'price']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['start_time', 'end_time']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['ticket']

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name']