
from django import template

register = template.Library()


@register.filter()
def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()
