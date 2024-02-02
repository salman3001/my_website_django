from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class common(models.Model):
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

    class Meta:
        abstract = True


class Category(common):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(
        max_length=150,
        unique=True,
    )

    def __str__(self):
        return self.name


class Tag(common):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Blog(common):
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
        blank=True,
        related_name="blogs",
        verbose_name="tags",
    )

    def __str__(self):
        return self.name
