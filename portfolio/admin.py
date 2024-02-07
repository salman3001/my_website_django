from django.contrib import admin
from . import models
from adminsortable2.admin import (
    SortableAdminMixin,
    SortableTabularInline,
    SortableStackedInline,
    SortableAdminBase,
)

# Register your models here.


class SkillTabularInline(SortableTabularInline):
    model = models.Skill


@admin.register(models.SkillCategory)
class SkillCategoryModelAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [SkillTabularInline]


@admin.register(models.Skill)
class SkillModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


# class ProjectTabularInline(SortableTabularInline):
#     model = models.Project


@admin.register(models.Tag)
class TagModelAdmin(SortableAdminBase, admin.ModelAdmin):
    pass


@admin.register(models.Project)
class ProjectModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
