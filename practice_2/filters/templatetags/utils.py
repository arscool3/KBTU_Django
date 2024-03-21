from django import template

register = template.Library()

@register.filter(name='unique')
def unique(value):
    """Removes duplicates from a list."""
    return list(set(value))
