from django import template
from menu.models import MainMenu, Menu

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(title=None):
    menu_items = MainMenu.objects.prefetch_related('sub_menu').filter(menu__title=title).filter(parent=None)
    return {'menu_items': menu_items}
