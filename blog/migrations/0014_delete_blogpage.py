# Generated by Django 2.2.9 on 2019-12-24 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('blog', '0013_auto_20191224_0631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPage',
        ),
    ]