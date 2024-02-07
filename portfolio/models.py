from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class SkillCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(
        upload_to="portfolio/skill_images",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        SkillCategory,
        related_name="skills",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    progress = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    meta_title = models.CharField(
        max_length=70,
        blank=True,
        null=True,
    )
    meta_keywords = models.CharField(max_length=70, blank=True, null=True)
    meta_desc = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Meta description"
    )
    meta_struct_data = models.CharField(
        max_length=400, blank=True, null=True, verbose_name="Structured data"
    )
    meta_image = models.ImageField(
        upload_to="portfolio/meta_images",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=150,
        unique=True,
    )
    short_desc = models.CharField(max_length=150, blank=True, null=True)
    content = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(
        upload_to="blog_images",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
        blank=True,
    )
    published = models.BooleanField(default=False, blank=True)
    featured = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0, editable=False, db_index=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="projects",
        verbose_name="tags",
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
