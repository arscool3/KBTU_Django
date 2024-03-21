from django import template
from django.utils.html import mark_safe

register = template.Library()

@register.filter
def lower(obj):
    return str(obj).lower()

@register.filter
def upper(name):
    return str(name).upper()

@register.filter
def add_list(name):
    return f'{name} list'

