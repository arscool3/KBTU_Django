from django import template
import datetime

register = template.Library()

@register.filter(name='capitalize')
def capitalize(value):
    return value.capitalize()

@register.filter(name='get_birth_year')
def get_birth_year(value):
    return datetime.datetime.now().year - value
