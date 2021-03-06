# Generated by Django 3.0.5 on 2020-08-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moon', '0016_auto_20200825_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='locality',
            field=models.CharField(max_length=60, null=True, verbose_name='localite'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(null=True, verbose_name='Montant total (EUR)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_quantity',
            field=models.IntegerField(null=True, verbose_name="Nombre d'articles"),
        ),
    ]
