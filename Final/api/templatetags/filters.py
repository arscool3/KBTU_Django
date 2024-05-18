from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def currency(value):
    return "${:,.2f}".format(value)

@register.filter
def italic(value):
    return mark_safe(f'<em>{value}</em>')