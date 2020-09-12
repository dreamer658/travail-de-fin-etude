from django.db import models
from moon.models.gender import Gender
from django.contrib.auth.models import User


class Customer(models.Model):
    """Model definition for Customer."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="Utilisateur")
    firstname = models.CharField(max_length=60, null=True, blank=True, verbose_name="Prénom")
    lastname = models.CharField(max_length=60, null=True, blank=True, verbose_name="Nom de famille")
    email = models.EmailField(max_length=60, null=True, blank=True, verbose_name="Email")
    date_of_birth = models.DateField(auto_now_add=True, null=True, blank=True,verbose_name="Date de naissance")
    device = models.CharField(max_length=200, null=True, blank=True)

    class Meta:

        """Meta definition for Customer."""

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['lastname', 'firstname']

    def __str__(self):
        """Unicode representation of Customer."""

        return "[{}] {} {} ".format(
                self.pk,
                self.firstname,
                self.lastname,
            )
