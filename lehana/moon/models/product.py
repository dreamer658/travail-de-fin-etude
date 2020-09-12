from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from moon.models.gender import Gender
from mptt.models import MPTTModel, TreeForeignKey




class Maker(models.Model):
    """ Model definition for Maker """

    name = models.CharField(max_length=60,verbose_name="Fabricant")
    phone = models.CharField(max_length=60, verbose_name="Telephone")
    email = models.CharField(max_length=60, verbose_name="Email")
    country = models.CharField(max_length=60, verbose_name="Pays")

    class Meta:
        """ Meta definition for Maker """

        verbose_name = "Fabricant"
        verbose_name_plural = "Fabricants"

    def __str__(self):
        return  "[{}] {} {}".format(self.pk, self.name, self.country)


class Category(MPTTModel):
    name = models.CharField(max_length=60, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
    slug = models.SlugField()

    class MPTTMeta:
        unique_together = (('parent', 'slug'))
        verbose_name_plural = 'categories'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))

        return slugs

    def get_absolute_url(self):
        """Return absolute url for Location."""

        return reverse('mpttcategory', kwargs={'slug': self.slug})


    def __str__(self):
        return self.name



class Product(models.Model):
    """Model definition for UserProfile.
    """

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=60, verbose_name="Nom de produit")
    stock = models.IntegerField(default = 0, verbose_name="Nombre d'articles")
    price = models.FloatField(verbose_name="Prix (EUR)")
    image = models.URLField(max_length=255, null=True, blank=True, verbose_name="URL image produit")
    color = models.CharField(max_length=60, verbose_name="Couleur")
    material = models.CharField(max_length=60, verbose_name="matière")
    description = models.TextField(verbose_name="Description")
    slug = models.SlugField()
    #is_liked = models.CharField(max_length=60,default="false", verbose_name="is_liked")
    is_liked = models.BooleanField(default=False, verbose_name='is_liked')
    favourites = models.ManyToManyField(User, related_name='favourite', blank=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['name']

    def get_absolute_url(self):
        """Return absolute url for Representation."""

        return reverse('ProdDetailTest', kwargs={'pk': self.pk})

    def get_slug_list_for_categories(self):
        try:
            ancestors = self.category.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]

        slugs = []

        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))

        return slugs


    def __str__(self):
        """ Unicode representation of Product. """

        return "[{}] {} {} {} {} {}".format(self.pk, self.gender.gender_name, self.name, self.stock, self.price, self.color)





class Shoes(models.Model):
    """Model definition for Shoes.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Produit")
    size_number = models.CharField(max_length=60, verbose_name="Taille")


    class Meta:
        """ Meta definition for Shoes"""
        verbose_name = "Chaussure"
        verbose_name_plural = "Chaussures"

    def __str__(self):
        """Unicode representation of Shoes."""

        return "[{}] {} {} ".format(self.pk, self.product.name, self.size_number)

class Clothes(models.Model):
    """Model definition for Clothes.
    """

    product = models.OneToOneField(Product, on_delete=models.CASCADE,verbose_name="Produit")
    size_letter = models.CharField(max_length=60, verbose_name="Taille lettre")
    size_digit = models.CharField(max_length=60, verbose_name="Taille nombre",blank=True)

    class Meta:
        """ Meta definition for Clothes"""
        verbose_name = "Vetement"
        verbose_name_plural = "Vetements"

    def __str__(self):
        """Unicode representation of Shoes."""

        return "[{}] {} {}".format(self.pk, self.product.name, self.size_letter, self.size_digit)

class Accessory(models.Model):
    """Model definition for Accessory.
    """

    product = models.OneToOneField(Product, on_delete=models.CASCADE,verbose_name="Produit")
    width = models.CharField(max_length=60, verbose_name="Largeur")
    thickness = models.CharField(max_length=60, verbose_name="Epaisseur")

    class Meta:
        """ Meta definition for Accessory"""
        verbose_name = "Accessoire"
        verbose_name_plural = "Accessoires"

    def __str__(self):
        """Unicode representation of Accessoire."""

        return "[{}] {} {} ".format(self.pk, self.product.name, self.width)

class Brand(models.Model):
    """Model definition for Brand.
    """

    maker = models.ForeignKey(Maker, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    brand_name = models.CharField(max_length=60, verbose_name="Marque")
    origin_country = models.CharField(max_length=60, verbose_name="Pays origine")

    class Meta:
        """ Meta definition for Brand"""
        verbose_name = "Marque"
        verbose_name_plural = "Marques"

    def __str__(self):
        return "[{}] {} {}".format(self.pk, self.brand_name, self.origin_country)


class Look(models.Model):
    """Model defitnition for Look"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    look = models.CharField(max_length=60, verbose_name="Look")

    class Meta:
        """ Meta definition for Look """

        verbose_name = "Look"
        verbose_name_plural = "Looks"

    def __str__(self):
        return  "[{}] {} {}".format(self.pk, self.look, self.product.name)
