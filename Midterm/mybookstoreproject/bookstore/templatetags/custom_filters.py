# custom_filters.py

from django import template
from django.template.defaultfilters import truncatechars
from django.utils.dateformat import format

register = template.Library()

@register.filter
def custom_date_format(value, arg):
    return format(value, arg)

@register.filter
def custom_truncate_chars(value, arg):
    return truncatechars(value, arg)
