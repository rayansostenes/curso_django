from django import template
from django.utils.html import mark_safe
from datetime import date

register = template.Library()


@register.filter
def to_json(value, global_name='foo'):
    return mark_safe('<script>{} = {};</script>'.format(global_name, value))

def lower_case(value):
    return str(value).lower()

@register.filter
def title_case(value):
    return mark_safe(str(value).title())

@register.filter
def upper_case(value):
    return str(value).upper()

@register.filter
def cut(value, arg):
    return str(value).replace(arg, '')

register.filter('lower_case', lower_case)
