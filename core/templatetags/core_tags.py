from django import template
from urllib.parse import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def get_query_string(context, **kwargs):
    return context["request"].GET.urlencode()


@register.simple_tag(takes_context=True)
def get_query_string_excluding(context, *args):
    query_dict = context["request"].GET.copy()

    for element in args:
        query_dict.pop(element, None)

    return urlencode(query_dict)


@register.simple_tag(takes_context=True)
def current_page_is(context, page_to_compare: int):
    query_dict: dict = context["request"].GET.copy()
    current_page = query_dict.get("page", None)

    return (
        True
        if current_page is not None and int(current_page) == page_to_compare
        else False
    )
