from django import template
from ..models import *

register = template.Library()


@register.inclusion_tag('app/menu.html')
def ShowMenu(isLoged):
    if isLoged == 1:
        menu = [{'title': 'Главная', 'link': 'home'}, {'title': 'Войти', 'link': 'login'}, {'title':'Зарегистрироваться', 'link' : 'reg'}]
    else:
        menu = [{'title': 'Главная', 'link': 'home'}, {'title': 'Мой профиль', 'link': 'me'}, {'title': 'Выйти', 'link': 'logout'}]
    return {'menu': menu}


@register.inclusion_tag('app/menu2.html')
def ShowMenu2():
    menu2 = [{'title': 'Группы', 'link': 'groups'}, {'title': 'Люди', 'link': 'people'}]
    return {'menu2': menu2}

@register.filter
def dateTime(d):
    return d.strftime('%d/%m/%Y %H:%m')


# Post
@register.filter
def postimage(pid):
    return Image.objects.getPostImage(pid).photo.url

@register.filter
def AuthorName(pus):
    info = UserInfo.objects.getinfo(pus.id)
    return info.name + ' ' + info.surname

@register.filter
def ava(pus):
    info = UserInfo.objects.getinfo(pus.id)
    return info.photo.url


@register.filter
def likes(p_id):
    return Like.objects.amount(p_id)

@register.filter
def coms(p_id):
    return Comment.objects.amount(p_id)

#People
def peopleinfo(p):
    return UserInfo.objects.getinfo(p.id)

@register.filter
def peopleimage(p):
    pi = peopleinfo(p)
    return pi.photo.url

@register.filter
def peoplename(p):
    pi = peopleinfo(p)
    return pi.name + ' ' + pi.surname

# Group
@register.filter
def subs(g):
    return Subscription.objects.amount(g)


