from django.urls import path

from .views import get_bombs,get_terrorists,get_counter_terrorists,get_counter_strike_games,add_counter_strike_game,add_terrorist,add_bomb,add_counter_terrorist,get_units,add_unit

urlpatterns = [
    path("bombs/", get_bombs),
    path("counter_terrorists/", get_counter_terrorists),
    path("terrorists/", get_terrorists),
    path("units/", get_units),
    path("counter_strike_games/", get_counter_strike_games),
    path("add_counter_terrorist/", add_counter_terrorist, name='add_counter_terrorist'),
    path("add_terrorist/", add_terrorist, name='add_terrorist'),
    path("add_bomb/", add_bomb, name='add_bomb'),
    path("add_unit/", add_unit, name="add_unit"),
    path("add_counter_strike_game/", add_counter_strike_game, name='add_counter_strike_game'),
]