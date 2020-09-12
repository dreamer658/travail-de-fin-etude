from django.db import models

class Gender(models.Model):
    """Model definition for UserProfile.
    """

    gender_name = models.CharField(max_length=60, verbose_name="Genre")

    class Meta:
        """Meta definition for UserProfile."""
        verbose_name = 'Genre d\'utilisateur'
        verbose_name_plural = 'Genres d\'utilisateur'

    def __str__(self):
        """Unicode representation of Gender."""

        return "{} {}".format(self.pk, self.gender_name)
