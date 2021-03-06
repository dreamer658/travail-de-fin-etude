# Generated by Django 3.0.5 on 2020-09-08 16:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moon', '0021_auto_20200903_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
