from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()

@register.filter
def converter(value: float):
    return round(value/450)