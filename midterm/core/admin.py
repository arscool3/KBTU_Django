from django.contrib import admin

# Register your models here.
from .models import Terrorist,CounterTerrorist,Bomb,CounterStrikeGame,Unit, Hostage_or_Bot,Map, Weapon
admin.site.register(Weapon)
admin.site.register(Map)
admin.site.register(Terrorist)
admin.site.register(CounterTerrorist)
admin.site.register(Bomb)
admin.site.register(CounterStrikeGame)
admin.site.register(Unit)
admin.site.register(Hostage_or_Bot)
