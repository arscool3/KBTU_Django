from django import template

register = template.Library()

@register.filter
def image_url(image_name):
    return f"../images/{image_name}"

@register.filter
def format_price(price):
    return "${:.2f}".format(price)