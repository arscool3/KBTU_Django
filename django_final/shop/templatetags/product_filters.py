from django import template

register = template.Library()

@register.filter(name='format_price')
def format_price(price):
    return "${:.2f}".format(price)

@register.filter(name='truncate_description')
def truncate_description(description, max_length=100):
    if len(description) <= max_length:
        return description
    else:
        return description[:max_length] + '...'

