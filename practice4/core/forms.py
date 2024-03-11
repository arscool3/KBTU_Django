from django import forms

from .models import CounterTerrorist, Terrorist, Bomb, CounterStrikeGame, Unit


class CounterTerroristForm(forms.ModelForm):
    class Meta:
        model = CounterTerrorist
        fields = '__all__'


class TerroristForm(forms.ModelForm):
    class Meta:
        model = Terrorist
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

class BombForm(forms.ModelForm):
    class Meta:
        model = Bomb
        fields = '__all__'


class CounterStrikeGameForm(forms.ModelForm):
    class Meta:
        model = CounterStrikeGame
        fields = '__all__'