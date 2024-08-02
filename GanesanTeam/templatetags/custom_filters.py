from django import template

register = template.Library()

@register.filter
def none_to_empty(value):
    return '' if value is None or value == 'None' else value