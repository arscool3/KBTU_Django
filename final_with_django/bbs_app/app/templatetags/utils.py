from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()

@register.filter
def get_date(value):
    if hasattr(value, "datetime"):
        return value.datetime.date()
    else:
        return None