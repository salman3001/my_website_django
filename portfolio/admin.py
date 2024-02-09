from django.contrib import admin
from . import models
from adminsortable2.admin import (
    SortableAdminMixin,
    SortableStackedInline,
    SortableAdminBase,
)

# Register your models here.


class SkillStackedInline(SortableStackedInline):
    model = models.Skill
    template = "adminsortable2/edit_inline/stacked-django-4.2.html"


@admin.register(models.SkillCategory)
class SkillCategoryModelAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        SkillStackedInline,
    ]
    fields = ["name"]


@admin.register(models.Skill)
class SkillModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ["name", "progress", "order"]
    list_editable = ["progress"]
    search_fields = ["name"]
    sortable_by = ["name", "progress"]
    pass


@admin.register(models.Tag)
class TagModelAdmin(SortableAdminBase, admin.ModelAdmin):
    pass


@admin.register(models.Project)
class ProjectModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["title", "image", "published", "featured", "updated_at", "order"]
    list_editable = ["featured", "published"]
    search_fields = ["title"]
    list_filter = ["featured", "published"]
    pass
