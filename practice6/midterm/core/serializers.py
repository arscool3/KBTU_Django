from rest_framework import serializers
from .models import CounterStrikeGame,CounterTerrorist,Terrorist,Map,Weapon,Bomb

class CounterStrikeGameSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CounterStrikeGame
        fields = '__all__'

class CounterTerroristSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterTerrorist
        fields = '__all__'

class TerroristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrorist
        fields = '__all__'

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'

class BombSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bomb
        fields = '__all__'



