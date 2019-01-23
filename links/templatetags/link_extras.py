from django import template

from links.models import Link, Category

register = template.Library()

@register.inclusion_tag('links/categories/category_nav.html')
def nav_category_list():
    ''' Returns dictionary of categories to place in nav '''
    category = Category.objects.all()
    return {'category': category}
