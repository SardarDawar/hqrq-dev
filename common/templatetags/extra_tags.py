from django import template
from projects.params import COUNT_MAX_RECENT_PROJECTS

register = template.Library()

@register.filter
def get_dict_item(dictionary, key):
    try:
        return dictionary.get(key)
    except :
        return None

@register.filter
def cool_number(value, num_decimals=1):
    if not value:
        return 0
    int_value = int(value)
    formatted_number = '{{:.{}f}}'.format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value/1000.0).rstrip('0.') + 'k'
    elif int_value < 1000000000:
        return formatted_number.format(int_value/1000000.0).rstrip('0.') + 'm'
    elif int_value < 1000000000000:
        return formatted_number.format(int_value/1000000000.0).rstrip('0.') + 'b'
    else:
        return formatted_number.format(int_value/1000000000000.0).rstrip('0.') + 't'

@register.filter
def cool_number_upper(value, num_decimals=1):
    return cool_number(value, num_decimals).upper()

@register.simple_tag
def subtract(value, arg):
    return value - arg

@register.simple_tag
def subtract_and_cool_number(value, arg, num_decimals=1):
    return cool_number(value-arg, num_decimals)

@register.filter
def get_user_recent_projects(user):
    return user.projects.all()[:COUNT_MAX_RECENT_PROJECTS]
