from django import template
register = template.Library()


@register.filter(name='save_url')
def save_url(url):
    print url
    return url
