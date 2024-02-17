from django import template

register = template.Library()

@register.filter(is_safe=True, name="format_phone")
def add_xx(value):
    return "%sxx" % value
