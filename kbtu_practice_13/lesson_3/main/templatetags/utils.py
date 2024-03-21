import dataclasses
from typing import NewType, Any

from django import template

register = template.Library()


@register.filter
def func(name: str) -> str:
    return name.lower()


@register.filter
def your_filter(*args, **kwargs) -> Any:
    return Any
