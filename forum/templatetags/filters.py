from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='addParams')
def add_params(value, arg):
    """Removes all values of arg from the given string"""
    return mark_safe(value.replace('0000', str(arg)))
