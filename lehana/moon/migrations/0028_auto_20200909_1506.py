# Generated by Django 3.0.5 on 2020-09-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0027_auto_20200909_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_liked',
            field=models.BooleanField(default=False, verbose_name='is_liked'),
        ),
    ]
