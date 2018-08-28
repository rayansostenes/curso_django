from django import template
from datetime import datetime

register = template.Library()

@register.inclusion_tag('core/person_list_tag.html')
def person_table(pessoas):
    return {
        'pessoas': pessoas
    }

@register.inclusion_tag('generic_table.html')
def generic_table(obj_list, collumns):
    return {
        'obj_list': obj_list,
        'collumns': collumns,
    }

@register.simple_tag
def current_time(formato=''):
    return datetime.now().strftime(formato)

@register.filter
def get_attr(value, key):
    return getattr(value, key)