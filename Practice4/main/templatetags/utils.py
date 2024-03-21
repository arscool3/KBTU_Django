from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()


# for templates -> app/templates
# for filters -> app/templatetags