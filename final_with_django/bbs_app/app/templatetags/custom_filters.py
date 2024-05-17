from django import template

register = template.Library()

@register.filter
def capitalize(value):
    """Capitalizes the first letter of the value."""
    return value.capitalize()

@register.filter
def add_class(field, css_class):
    """Adds a CSS class to form fields."""
    return field.as_widget(attrs={"class": css_class})
