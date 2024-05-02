from django import template

register = template.Library()


@register.filter
def lower(value: str):
    return value.lower()


@register.filter
def filterO(value: str):
    if 'O' or 'o' in value:
        return value
    return value + ' FEEEEE'
