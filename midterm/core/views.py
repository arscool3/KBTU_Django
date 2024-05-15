from itertools import chain

from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import CounterTerrorist, Terrorist, Bomb, CounterStrikeGame, Unit, Map, Weapon, Hostage_or_Bot
from .forms import CounterTerroristForm, TerroristForm, BombForm, CounterStrikeGameForm, UnitForm, HostageOrBotForm, MapForm, WeaponForm

# POST Methods

def add_model(request, given_form, given_url, name):
    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    def __str__(self):
        return self.name

    return render(request, 'index2.html', {'form': given_form(), 'given_url': given_url})


def add_bomb(request):
    return add_model(request, BombForm, 'add_bomb', 'bomb')


def add_counter_terrorist(request):
    return add_model(request, CounterTerroristForm, 'add_counter_terrorist', 'counter_terrorist')


def add_counter_strike_game(request):
    return add_model(request, CounterStrikeGameForm, 'add_counter_strike_game', 'counter_strike_game')


def add_unit(request):
    return add_model(request, UnitForm, 'add_unit', 'unit')


def add_map(request):
    return add_model(request, MapForm, 'add_map', 'map')


def add_weapon(request):
    return add_model(request, WeaponForm, 'add_weapon', 'weapon')


def add_bot(request):
    return add_model(request, HostageOrBotForm, 'add_bot', 'bot')


def add_terrorist(request):
    return add_model(request, TerroristForm, 'add_terrorist', 'terrorist')


# GET Methods

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
    return render(request, 'tt_team_info.html', {"iterable": terrorists, "object": "Terrorists"})


def get_bombs(request):
    bombs = Bomb.objects.all()
    if bomb_name := request.GET.get('bomb_name'):
        bombs = bombs.filter(name__icontains=bomb_name.capitalize())

    # Apply the custom queryset method to retrieve terrorists who planted the bombs
    bombs_with_planted_terrorists = bombs.get_planted_terrorist()

    return render(request, 'bombs.html', {"iterable": bombs_with_planted_terrorists, "object": "Bombs"})




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
    return render(request, 'ct_team_info.html', {"iterable": counter_terrorists, "object": "Counter Terrorists"})



def get_maps(request):
    maps = Map.objects
    if map_name := request.GET.get('map_name'):
        maps = maps.filter(map__name=map_name.capitalize())

    maps = maps.all()
    return render(request, 'index.html', {"iterable": maps, "object": "Maps"})


def games_by_map(request, map_name):
    map_instance = get_object_or_404(Map, name=map_name)
    games = CounterStrikeGame.objects.filter(map=map_instance)

    return render(request, 'games_by_map.html', {'games': games, 'map_name': map_name})


def get_weapons(request):
    weapons = Weapon.objects
    if weapon_name := request.GET.get('weapon_name'):
        weapons = weapons.filter(weapon__name=weapon_name.capitalize())

    weapons = weapons.all()
    return render(request, 'index.html', {"iterable": weapons, "object": "Weapons"})



def get_bots(request):
    bots = Hostage_or_Bot.objects
    if bot_name := request.GET.get('bot_name'):
        bots = bots.filter(bot__name=bot_name.capitalize())

    bots = bots.all()
    return render(request, 'index.html', {"iterable": bots, "object": "Bots"})


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)


def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")


@login_required
def create_game(request):
    if request.method == 'POST':
        form = CounterStrikeGameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            messages.success(request, 'Game created successfully!')
            return redirect('index')  # Redirect to the homepage or wherever appropriate
    else:
        form = CounterStrikeGameForm()
    return render(request, 'create_game.html', {'form': form})


def game_info(request, game_name):
    game = CounterStrikeGame.objects.get(name=game_name)
    terrorists = game.terrorist_set.all().select_related('unit')
    counter_terrorists = game.counterterrorist_set.all().select_related('unit')
    players = list(chain(terrorists, counter_terrorists))
    context = {
        'game': game,
        'players': players,
    }
    return render(request, 'game_info.html', context)
