from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from . import models

# Register your models here.


@admin.register(models.Blog)
class BlogModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "published",
        "featured",
        "order",
    ]

    list_editable = [
        "slug",
    ]


@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]

    list_editable = [
        "slug",
    ]


admin.site.register(models.Tag)
