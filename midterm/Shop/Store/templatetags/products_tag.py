from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('Store/cat_list.html')
def ShowCats():
    cats = Category.objects.all()
    return {'cats': cats}

@register.inclusion_tag('Store/menu.html')
def ShowMenu(isLoged):
    if isLoged == 1:
        menu = [{'title': 'Главная', 'link': 'home'}, {'title': 'Войти', 'link': 'login'}, {'title':'Зарегистрироваться', 'link' : 'reg'}]
    else:
        menu = [{'title': 'Главная', 'link': 'home'}, {'title': 'Моя Корзина', 'link': 'busket'}, {'title': 'Мои Покупки', 'link': 'purchases'}]
    return {'menu': menu}

@register.filter
def dateTime(d):
    return d.strftime('%d/%m/%Y %H:%m')

@register.filter
def isAuthMenu(v):
    return v[1]['title'] != 'Войти'

@register.filter
def adress1(a):
    return f'{a.country}, г. {a.city}'

@register.filter
def adress2(a):
    return f'{a.country}, г. {a.city}' \
            f' ул. {a.street}, дом {a.house}'