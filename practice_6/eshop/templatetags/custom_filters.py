from django import template

register = template.Library()


@register.filter(name='format_price')
def format_price(value):
    return "${:.2f}".format(value)


@register.filter(name='shorten_name')
def shorten_name(value, length=10):
    if len(value) > length:
        return value[:length] + '...'
    return value
