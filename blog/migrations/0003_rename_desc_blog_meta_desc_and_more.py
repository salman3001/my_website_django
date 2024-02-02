# Generated by Django 5.0.1 on 2024-02-01 22:38

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='desc',
            new_name='meta_desc',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='keywordz',
            new_name='meta_keywords',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='meta_desc',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='keywordz',
            new_name='meta_keywords',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='meta_title',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='desc',
            new_name='meta_desc',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='keywordz',
            new_name='meta_keywords',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='meta_title',
        ),
        migrations.AddField(
            model_name='blog',
            name='meta_title',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='blog.tag', verbose_name='tags'),
        ),
    ]