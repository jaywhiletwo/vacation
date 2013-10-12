from django import template

register = template.Library()

@register.inclusion_tag('_menu_list.html', takes_context=True)
def draw_menu(context, obj_type, obj_list, menu_section_name):
    try:
        active_check = context['active_type'] == obj_type
        active_id = context['active_id']
    except KeyError:
        active_check = False
        active_id = None

    return {
        'menu_item_type': menu_section_name,
        'menu_item_list': obj_list,
        'active_check': active_check,
        'active_id': active_id,
    }
