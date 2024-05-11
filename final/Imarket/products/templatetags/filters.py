from django import template
from django.utils.dateformat import DateFormat

register = template.Library()

@register.filter(name='truncate_description')
def truncate_description(description, length):
    if description is None:
        return ''
    if len(description) > length:
        return description[:length] + '...'
    return description

@register.filter(name='format_created_at')
def format_created_at(created_at, format_string):
    df = DateFormat(created_at)
    return df.format(format_string)