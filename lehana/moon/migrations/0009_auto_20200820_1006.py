# Generated by Django 3.0.5 on 2020-08-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0008_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True, verbose_name='num de commande'),
        ),
    ]
