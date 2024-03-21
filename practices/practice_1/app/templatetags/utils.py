from django import template

register = template.Library()


@register.filter
def capitalize(value: str) -> str:
    return value.capitalize()


@register.filter
def age_classifier(age: int) -> str:
    age_c = ""
    if 0 <= age <= 10:
        age_c =  "kid"
    elif 10 <= age <= 19:
        age_c = "teenager"
    elif 20 <= age <= 55:
        age_c = "adult"
    else:
        age_c = "older"

    return f"{age}({age_c})"
