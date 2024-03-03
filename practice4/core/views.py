
from django.http import HttpResponse
from django.shortcuts import render

from .models import CounterTerrorist, Terrorist, Bomb, CounterStrikeGame, Unit
from .forms import CounterTerroristForm, TerroristForm, BombForm, CounterStrikeGameForm, UnitForm


def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index2.html', {'form': given_form(), 'given_url': given_url})


def add_bomb(request):
    return add_model(request, BombForm, 'add_bomb', 'bomb')


def add_counter_terrorist(request):
    return add_model(request, CounterTerroristForm, 'add_counter_terrorist', 'counter_terrorist')


def add_counter_strike_game(request):
    return add_model(request, CounterStrikeGameForm, 'add_counter_strike_game', 'counter_strike_game')

def add_unit(request):
    return add_model(request, UnitForm, 'add_unit', 'unit')

def add_terrorist(request):
    return add_model(request, TerroristForm, 'add_terrorist', 'terrorist')


# def get_units(request):
#     units = Unit.objects.all()
#     return render(request, 'index.html', {'units':units})

def get_units(request):
    units = Unit.objects
    if unit_name := request.GET.get('unit_name'):
        units = units.filter(unit__name=unit_name.capitalize())

    units = units.all()
    return render(request, 'index.html', {"iterable": units, "object": "Units"})

def get_terrorists(request):
    terrorists = Terrorist.objects
    if terrorist_name := request.GET.get('terrorist_name'):
        terrorists = terrorists.filter(terrorist__name=terrorist_name.capitalize())

    terrorists = terrorists.all()
    return render(request, 'index.html', {"iterable": terrorists, "object": "Terrorists"})

def get_bombs(request):
    bombs = Bomb.objects
    if bomb_name := request.GET.get('bomb_name'):
        bombs = bombs.filter(bomb__name=bomb_name.capitalize())

    terrorists = bombs.all()
    return render(request, 'index.html', {"iterable": terrorists, "object": "Bombs"})



def get_counter_strike_games(request):
    counter_strike_games = CounterStrikeGame.objects
    if counter_strike_game_name := request.GET.get('counter_strike_game_name'):
        counter_strike_games = counter_strike_games.filter(counter_strike_game__name=counter_strike_game_name.capitalize())

    counter_strike_games = counter_strike_games.all()
    return render(request, 'index.html', {"iterable": counter_strike_games, "object": "Counter Strike Game"})

def get_counter_terrorists(request):
    counter_terrorists = CounterTerrorist.objects
    if counter_terrorist_name := request.GET.get('counter_terrorist_name'):
        counter_terrorists = counter_terrorists.filter(counter_terrorist__name=counter_terrorist_name.capitalize())

    counter_terrorists = counter_terrorists.all()
    return render(request, 'index.html', {"iterable": counter_terrorists, "object": "Counter Terrorists"})
