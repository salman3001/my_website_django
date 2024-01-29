from django.db import models

# Create your models here.


class Seo(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    keyword = models.CharField(max_length=70, blank=True, null=True)
    desc = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(
        upload_to="seo/images", max_length=70, blank=True, null=True
    )
    struct_data = models.CharField(max_length=400, blank=True, null=True)
