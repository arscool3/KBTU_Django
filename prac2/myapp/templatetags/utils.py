from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()

@register.filter
def add_suffix(value: str) -> str:
    return f"{value} Junior"

# for templates -> app/templates
# for filters -> app/templatetags