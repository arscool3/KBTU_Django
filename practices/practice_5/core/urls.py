from django.urls import path

from .views import get_clan_by_name, get_castle, get_dragons, get_heroes, add_hero, add_clan, add_castle, add_dragon

urlpatterns = [
    path("clans/", get_clan_by_name),
    path("castles/", get_castle),
    path("dragons/", get_dragons),
    path("heroes/", get_heroes),
    path("add_hero/", add_hero, name='add_hero'),
    path("add_clan/", add_clan, name='add_clan'),
    path("add_dragon/", add_dragon, name='add_dragon'),
    path("add_castle/", add_castle, name='add_castle'),
]