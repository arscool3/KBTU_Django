from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()


