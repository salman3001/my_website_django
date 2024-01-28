from django.db import models

# Create your models here.


class Blog(models.Model):
    title = (models.CharField(max_length=150, unique=True),)
    slug = models.SlugField(
        max_length=150,
        unique=True,
        help_text="This will be auto generated if you dont add it",
    )
    short_desc = (models.CharField(max_length=150),)
    image = (
        models.ImageField(
            upload_to="blog_images",
            height_field=None,
            width_field=None,
            max_length=None,
            null=True,
            blank=True,
        ),
    )
