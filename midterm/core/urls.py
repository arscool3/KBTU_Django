from django.urls import path

from .views import get_bombs, get_terrorists, get_counter_terrorists, get_counter_strike_games, add_counter_strike_game, \
    add_terrorist, add_bomb, add_counter_terrorist, get_units, add_unit, get_maps, get_bots, get_weapons, add_bot, \
    add_map, add_weapon, register_view, login_view, check_view, logout_view, create_game, games_by_map, game_info

urlpatterns = [
    path("bombs/", get_bombs),
    path("counter_terrorists/", get_counter_terrorists),
    path("terrorists/", get_terrorists),
    path("units/", get_units),
    path("maps/", get_maps),
    path("bots/", get_bots),
    path("weapons/", get_weapons),
    path("counter_strike_games/", get_counter_strike_games),
    path("add_counter_terrorist/", add_counter_terrorist, name='add_counter_terrorist'),
    path("add_terrorist/", add_terrorist, name='add_terrorist'),
    path("add_bomb/", add_bomb, name='add_bomb'),
    path("add_unit/", add_unit, name="add_unit"),
    path("add_bot/", add_bot, name="add_bot"),
    path("add_map/", add_map, name="add_map"),
    path("add_weapon/", add_weapon, name="add_weapon"),
    path("add_counter_strike_game/", add_counter_strike_game, name='add_counter_strike_game'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path("logout/", logout_view, name='logout'),
    path("create_game/", create_game), # I will refine it in the future
    path("games_by_map/<str:map_name>/", games_by_map, name='games_by_map'),
    path("game_info/<str:game_name>/", game_info, name='game_info'),

]