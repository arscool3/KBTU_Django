from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()

@register.filter
def currency(value: str) -> str:
    return f"{value} $"
