from django import template


register = template.Library()

@register.filter
def lower(name):
    return name.lower()

@register.filter
def reverse(name):
    return name[::-1]