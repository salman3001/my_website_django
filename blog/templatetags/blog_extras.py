from django import template

register = template.Library()


@register.inclusion_tag("blog/paginate.html")
def paginate_blogs(blogs):
    return {"blogs": blogs}
