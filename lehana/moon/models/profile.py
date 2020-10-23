from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from moon.models.customer import Customer
from moon.models.product import Product
from moon.models.gender import Gender


class Discount (models.Model):
    """Model definition for a discount"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True, verbose_name="Utilisateur")

    class Meta:
        """ Meta definition of Discount """
        verbose_name = "Reduction"
        verbose_name_plural = "Reductions"

    def __str__(self):
        return "[{}] {} ".format(self.pk, self.product.name)


class UserProfile(models.Model):
    """Model definition for UserProfile.
    """
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="Utilisateur")
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, verbose_name="Client")
    discount_rate = models.IntegerField(default=0, blank=True, null=True)
    discount = models.ManyToManyField(Discount, related_name='discount', blank=True)
    got_a_discount = models.BooleanField(default=False, null=True, blank=True)
    flag_discount = models.BooleanField(default=False, null=True, blank=True)
    birthday = models.CharField(max_length=60,null=True, blank=True)

    # Faire la fonction d'incrementation lorsqu'il y a un achat.

    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = 'Profil d\'utilisateur'
        verbose_name_plural = 'Profils d\'utilisateur'

    def __str__(self):
        """Unicode representation of UserProfile."""

        return "[{}] Profile de {}".format(self.pk, self.user.username)

    def get_absolute_url(self):
        return reverse('edit-profile')

    @receiver(post_save, sender=User)
    def user_profile(sender, **kwargs):
        user = kwargs.get('instance')
        created = kwargs.get('created')
        if created:
            UserProfile.objects.create(user=user)

class Favorite(models.Model):
    """Model definition for Favorite """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    class Meta:
        """Meta definition for Favorite."""
        verbose_name = 'favori'
        verbose_name_plural = 'favoris'

    def __str__(self):
        """Unicode representation of Favorite."""

        return "{} {} {}".format(self.pk, self.user.username, self.product.name)

class Comment(models.Model):
    """Model definition for a comment"""
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name="description")
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def get_absolute_url(self):
        """Return absolute url for comment."""

        return reverse('commentView', kwargs={'pk': self.pk})

    def __str__(self):
        """Unicode representation of Favorite."""

        return "[{}] {} {} {} {}".format(self.pk, self.product.name, self.user.username, self.description, self.date)
