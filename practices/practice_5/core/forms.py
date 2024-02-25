from django import forms

from .models import Castle, Clan, Hero, Dragon


class CastleForm(forms.ModelForm):
    class Meta:
        model = Castle
        fields = '__all__'


class ClanForm(forms.ModelForm):
    class Meta:
        model = Clan
        fields = '__all__'


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'


class DragonForm(forms.ModelForm):
    class Meta:
        model = Dragon
        fields = '__all__'

