from django import forms
from .models import *

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

class MembershipPlanForm(forms.ModelForm):
    class Meta:
        model = MembershipPlan
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class WorkoutFilterByTrainerForm(forms.Form):
    trainer = forms.ModelChoiceField(queryset=Trainer.objects.all(), empty_label="All Trainers", required=False, label="Trainer")

    def filter_workouts(self):
        trainer = self.cleaned_data.get('trainer')

        workouts = Workout.objects.all()

        if trainer:
            workouts = workouts.filter(trainer=trainer)

        return workouts

class WorkoutFilterByTypeForm(forms.Form):
    WORKOUT_TYPE_CHOICES = (
        ('cardio', 'Cardio'),
        ('strength', 'Strength Training'),
    )

    type = forms.ChoiceField(choices=WORKOUT_TYPE_CHOICES, required=False, label="Type")

    def filter_workouts(self):
        type = self.cleaned_data.get('type')

        workouts = Workout.objects.all()

        if type:
            workouts = workouts.filter(type=type)

        return workouts