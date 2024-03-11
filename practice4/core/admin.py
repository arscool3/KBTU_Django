from django.contrib import admin

# Register your models here.
from .models import Terrorist,CounterTerrorist,Bomb,CounterStrikeGame,Unit
admin.site.register(Terrorist)
admin.site.register(CounterTerrorist)
admin.site.register(Bomb)
admin.site.register(CounterStrikeGame)
admin.site.register(Unit)