from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()

@register.filter
def sort_by_name(value, key_name):
    return sorted(value, key=lambda x: x[key_name].lower())