from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline
from . import models

# Register your models here.


class BlogTabularInline(SortableTabularInline):
    model = models.Blog
    template = "adminsortable2/edit_inline/tabular-django-4.2.html"
    fields = ["title", "slug"]
    prepopulated_fields = {"slug": ["title"]}


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
        "featured",
        "published",
    ]

    fields = [
        "title",
        "slug",
        "short_desc",
        "content",
        "image",
        "published",
        "featured",
        "category",
        "tags",
        "meta_title",
        "meta_keywords",
        "meta_desc",
        "meta_struct_data",
    ]

    prepopulated_fields = {"slug": ["title"]}


@admin.register(models.Category)
class CategoryModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [BlogTabularInline]
    list_display = [
        "name",
        "slug",
    ]

    prepopulated_fields = {"slug": ["name"]}

    fields = [
        "name",
        "slug",
        "meta_title",
        "meta_keywords",
        "meta_desc",
        "meta_struct_data",
    ]


@admin.register(models.Tag)
class TagModelAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "slug",
        "meta_title",
        "meta_keywords",
        "meta_desc",
        "meta_struct_data",
    ]

    prepopulated_fields = {"slug": ["name"]}
