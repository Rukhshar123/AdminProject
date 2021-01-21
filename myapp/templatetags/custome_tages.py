from django import template

register=template.Library()

@register.simple_tag
def get_half_content(description):
    return description[:int(len(description)/5)]