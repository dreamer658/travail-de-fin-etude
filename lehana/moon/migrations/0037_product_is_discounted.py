# Generated by Django 3.0.5 on 2020-09-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0036_auto_20200917_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_discounted',
            field=models.BooleanField(default=False, verbose_name='is_discounted'),
        ),
    ]
