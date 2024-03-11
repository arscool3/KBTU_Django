from django import template

register = template.Library()


@register.filter
def capitalize_first_letter(value):
    return value.capitalize()


@register.filter
def replaceSpace(value):
    return '-'.join(value.split())
