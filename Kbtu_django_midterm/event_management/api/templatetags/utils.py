from django import template
from django.utils import formats

register = template.Library()

@register.filter
def format_time(value):
    return formats.date_format(value, "H:i:s")

@register.filter
def truncate_title(value):
    if len(value) > 20:
        return value[:20] + '...'
    return value
