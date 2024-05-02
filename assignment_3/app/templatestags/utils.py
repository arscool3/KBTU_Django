from django import template

register = template.Library()

@register.filter
def custom_function(value):
    return value**2
