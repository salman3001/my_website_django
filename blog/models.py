from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class common(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    keywordz = models.CharField(max_length=70, blank=True, null=True)
    desc = models.CharField(max_length=150, blank=True, null=True)
    struct_data = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        abstract = True


class Category(common):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(
        max_length=150,
        unique=True,
    )


class Tag(common):
    name = models.CharField(max_length=30, unique=True)


class Blog(common):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=150,
        unique=True,
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
