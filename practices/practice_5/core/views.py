
from django.http import HttpResponse
from django.shortcuts import render

from .models import Clan, Hero, Castle, Dragon
from .forms import ClanForm, CastleForm, HeroForm, DragonForm


def get_clan_by_name(request):
    clans = Clan.objects
    if name := request.GET.get('name'):
        clans = clans.filter(name=name.capitalize())
    clans = clans.all()
    return render(request, "index.html", {"iterable": clans, "object": "Clans"})


def get_castle(request):
    castles = Castle.objects
    if castle_name := request.GET.get('castle_name'):
        castles = castles.filter(castle__name=castle_name.capitalize())
    castles = castles.all()
    return render(request, 'index.html', {"iterable": castles, "object": "Castles"})


def get_dragons(request):
    dragons = Dragon.objects
    if dragon_name := request.GET.get('dragon_name'):
        dragons = dragons.filter(dragon__name=dragon_name.capitalize())

    if size := request.GET.get('size'):
        dragons = dragons.filter(size=size)

    dragons = dragons.all()

    return render(request, 'index.html', {"iterable": dragons, "object": "Dragons"})


def get_heroes(request):
    heroes = Hero.objects
    if hero_name := request.GET.get('hero_name'):
        heroes = heroes.filter(hero__name=hero_name.capitalize())

    heroes = heroes.all()
    return render(request, 'index.html', {"iterable": heroes, "object": "Heroes"})


def add_model(request, given_form, given_url, name):

    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index2.html', {'form': given_form(), 'given_url': given_url})


def add_clan(request):
    return add_model(request, ClanForm, 'add_clan', 'clan')


def add_hero(request):
    return add_model(request, HeroForm, 'add_hero', 'hero')


def add_castle(request):
    return add_model(request, CastleForm, 'add_castle', 'castle')


def add_dragon(request):
    return add_model(request, DragonForm, 'add_dragon', 'dragon')
