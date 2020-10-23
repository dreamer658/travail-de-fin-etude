# Generated by Django 3.0.5 on 2020-10-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0051_auto_20201017_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(null=True),
        ),
    ]