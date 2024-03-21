from django import template

register = template.Library()


@register.filter
def uppercase_name(value):
    if hasattr(value, 'name'):
        return value.name.upper()
    elif hasattr(value, 'title'):
        return value.title.upper()
    else:
        return str(value).upper()
