from django import template

register = template.Library()

@register.filter
def lower(value):
    """Converts a string into all lowercase."""
    return value.lower()

@register.filter
def business_title(value):
    """Appends 'Business' to the string."""
    return f"{value} Business"
