from django import template

register = template.Library()

@register.filter(name='datetime_format')
def datetime_format(value, format_string):
    return format(value, format_string)

@register.filter(name='parking_space_status')
def parking_space_status(value):
    if value:
        return "Occupied"
    else:
        return "Available"