from django import template

register = template.Library()



def update_variable(value):
    return value


update_variable = register.filter('update_variable', update_variable)