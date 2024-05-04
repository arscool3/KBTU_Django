from django import template

register = template.Library()

@register.filter
def reverse_string(value):
    return value[::-1]

@register.filter
def to_upper(value):
    return value.upper()


"""this just example to 2 filters for templates"""