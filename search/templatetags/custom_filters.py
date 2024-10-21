from django import template

register = template.Library()

@register.filter
def to(value):
    return range(1, value + 1)