from django import forms

from .models import CounterTerrorist, Terrorist, Bomb, CounterStrikeGame, Unit, Map, Weapon, Hostage_or_Bot


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


class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = '__all__'


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = '__all__'


class HostageOrBotForm(forms.ModelForm):
    class Meta:
        model = Hostage_or_Bot
        fields = '__all__'


class CounterStrikeGameForm(forms.ModelForm):
    class Meta:
        model = CounterStrikeGame
        fields = '__all__'