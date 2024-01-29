from django.db import models
from core.models import Seo
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    seo = models.OneToOneField(
        Seo, verbose_name="Seo", on_delete=models.CASCADE, blank=True, null=True
    )


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    seo = models.OneToOneField(
        Seo, verbose_name="Seo", on_delete=models.CASCADE, blank=True, null=True
    )


class Blog(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=150,
        unique=True,
        help_text="This will be auto generated if you dont add it",
    )
    short_desc = models.CharField(max_length=150, blank=True, null=True)
    content = RichTextField()
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
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="blogs",
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name="tags",
    )
    seo = models.OneToOneField(
        Seo,
        verbose_name="Seo",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
