from django import template

register = template.Library()

@register.filter

def lower(value:str):
    return value.lower()


@register.filter

def filterA(value:str):
    if 'A' or 'a' in value:
        return value
    return value+'a'
