# Generated by Django 3.0.5 on 2020-08-11 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60, verbose_name='Prénom')),
                ('lastname', models.CharField(max_length=60, verbose_name='Nom de famille')),
                ('street', models.CharField(max_length=60, verbose_name='Rue')),
                ('street_number', models.CharField(max_length=60, verbose_name='Numéro')),
                ('postal_code', models.CharField(max_length=60, verbose_name='Code postal')),
                ('mail', models.CharField(max_length=60, verbose_name='Email')),
                ('date_of_birth', models.DateField(auto_now_add=True, null=True, verbose_name='Date de naissance')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['lastname', 'firstname'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_name', models.CharField(max_length=60, verbose_name='Genre')),
            ],
            options={
                'verbose_name': "Genre d'utilisateur",
                'verbose_name_plural': "Genres d'utilisateur",
            },
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Fabricant')),
                ('phone', models.CharField(max_length=60, verbose_name='Telephone')),
                ('email', models.CharField(max_length=60, verbose_name='Email')),
                ('country', models.CharField(max_length=60, verbose_name='Pays')),
            ],
            options={
                'verbose_name': 'Fabricant',
                'verbose_name_plural': 'Fabricants',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nom de produit')),
                ('stock', models.PositiveIntegerField(verbose_name="Nombre d'articles")),
                ('price', models.FloatField(verbose_name='Prix (EUR)')),
                ('image', models.URLField(blank=True, max_length=255, null=True, verbose_name='URL image produit')),
                ('color', models.CharField(max_length=60, verbose_name='Couleur')),
                ('material', models.CharField(max_length=60, verbose_name='matière')),
                ('description', models.TextField(verbose_name='Description')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Gender')),
                ('maker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Maker')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=60, verbose_name='Statut')),
            ],
            options={
                'verbose_name': 'Statut',
                'verbose_name_plural': 'Statuts',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(blank=True, default=0, null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='moon.Customer', verbose_name='Client')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Gender')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': "Profil d'utilisateur",
                'verbose_name_plural': "Profils d'utilisateur",
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_number', models.CharField(max_length=60, verbose_name='Taille')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='moon.Product', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'Chaussure',
                'verbose_name_plural': 'Chaussures',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name="Nombre d'articles")),
                ('line_amount', models.FloatField(verbose_name='Montant de ligne (EUR)')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de commande')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Product')),
            ],
            options={
                'verbose_name': 'Produit de la commande',
                'verbose_name_plural': 'Produits de la commande',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.PositiveIntegerField(verbose_name="Nombre d'articles")),
                ('total_price', models.FloatField(verbose_name='Montant de ligne (EUR)')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Customer')),
                ('order_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.OrderItem')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Status')),
            ],
            options={
                'verbose_name': 'Commande',
                'verbose_name_plural': 'Commandes',
            },
        ),
        migrations.CreateModel(
            name='Look',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('look', models.CharField(max_length=60, verbose_name='Look')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Product')),
            ],
            options={
                'verbose_name': 'Look',
                'verbose_name_plural': 'Looks',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Order')),
            ],
            options={
                'verbose_name': 'Facture',
                'verbose_name_plural': 'Factures',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'favori',
                'verbose_name_plural': 'favoris',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_rate', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reduction',
                'verbose_name_plural': 'Reductions',
            },
        ),
        migrations.CreateModel(
            name='Deliverer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
                ('phone_number', models.CharField(max_length=60, verbose_name='Numero de telephone')),
                ('mail', models.CharField(max_length=60, verbose_name='Email')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Order')),
            ],
            options={
                'verbose_name': 'Livreur',
                'verbose_name_plural': 'Livreurs',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='description')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_letter', models.CharField(max_length=60, verbose_name='Taille lettre')),
                ('size_digit', models.CharField(blank=True, max_length=60, verbose_name='Taille nombre')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='moon.Product', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'Vetement',
                'verbose_name_plural': 'Vetements',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='moon.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=60, verbose_name='Marque')),
                ('origin_country', models.CharField(max_length=60, verbose_name='Pays origine')),
                ('maker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Maker')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moon.Product')),
            ],
            options={
                'verbose_name': 'Marque',
                'verbose_name_plural': 'Marques',
            },
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.CharField(max_length=60, verbose_name='Largeur')),
                ('thickness', models.CharField(max_length=60, verbose_name='Epaisseur')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='moon.Product', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'Accessoire',
                'verbose_name_plural': 'Accessoires',
            },
        ),
    ]
