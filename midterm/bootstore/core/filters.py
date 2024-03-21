from django import template

register = template.Library()

@register.filter
def capitalize_first(value):
    return value.capitalize()


@register.filter
def format_price(value):
    return f"${value:,.2f}"
