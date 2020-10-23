from django.db import models
from moon.models.customer import Customer
from moon.models.product import Product

class Status(models.Model):
    """ Model definition for Status """

    status = models.CharField(max_length=60, verbose_name="Statut")

    class Meta:
        """ Meta definition for Status. """
        verbose_name = "Statut"
        verbose_name_plural = "Statuts"

    def __str__(self):
        """ Unicode representation for status """
        return "[{}] {}".format(self.pk, self.status)


class Coupon(models.Model):

    """ Model definition for a coupon. """
    code = models.CharField(max_length=30, null=True, verbose_name="coupon")
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    class Meta:
        """ Meta definition for the coupon. """
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    def __str__(self):
        return "[{}] {}".format(self.pk, self.code)


class Order(models.Model):
    """ Method definition for OrderItem. """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)
    total_quantity = models.IntegerField(null=True, verbose_name="Nombre d'articles", blank=True)
    total_price = models.FloatField(null=True, verbose_name="Montant total (EUR)", blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    complete = models.BooleanField(default = False, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, null=True, verbose_name="num de commande", blank=True)
    been_discounted = models.BooleanField(default = False, blank=True, null=True)


    #Les methods pour ajouter etc.
    @property
    def get_cart_total(self):
        """ To get the total price of the cart. """
        orderitems = self.orderitem_set.all()# accès à l'autre coté de la ForeignKey
        total = sum([item.get_total for item in orderitems])
        if self.been_discounted:
            total = total-((total/100)*20)
        self.total_price = total
        return total

    @property
    def get_cart_items(self):
        """ To find out how many items in our cart. """

        orderitems = self.orderitem_set.all()# accès à l'autre coté de la ForeignKey
        total = sum([item.quantity for item in orderitems])
        self.total_quantity = total
        return total


    class Meta:
        """ Meta definition for Order. """

        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self):
        """Unicode representation of Order."""

        return " [{}] {} {}".format(self.pk, self.date, self.transaction_id)

class OrderItem(models.Model):
    """ Method definition for OrderItem. """

    order =  models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, verbose_name="Nombre d'articles")
    line_amount = models.FloatField(null=True,verbose_name="Montant de ligne (EUR)")
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True, verbose_name="Date de commande")

    class Meta:
        """ Meta definition for OrderItem. """

        verbose_name = "Produit de la commande"
        verbose_name_plural = "Produits de la commande"

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        """Unicode representation of Product."""

        return " [{}] {} ".format(self.pk, self.product.name)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    locality = models.CharField(max_length=60, null=True, verbose_name="localite")
    street = models.CharField(max_length=60, verbose_name="Rue")
    street_number = models.CharField(max_length=60, verbose_name="Numéro")
    postal_code = models.CharField(max_length=60, verbose_name="Code postal")
    city = models.CharField(max_length=60, verbose_name="Ville")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        """Meta definition for ShippingAddress."""

        verbose_name = 'Adresse livraison'
        verbose_name_plural = 'Adresses livraison'

    def __str__(self):
        return "{} {} {}".format(
            self.pk,
            self.street,
            self.street_number
        )




class Invoice(models.Model):
    """ Model definition for Invoice """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        """ Meta definition for Invoice. """
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    def __str__(self):
        """ Unicode representation for Invoice """
        return "[{}] {} {}".format(self.pk, self.order.total_price, self.date)


class Deliverer(models.Model):

    """ Model definition for Deliverer """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    name = models.CharField( max_length=60, verbose_name="Nom")
    phone_number = models.CharField( max_length=60, verbose_name="Numero de telephone")
    mail = models.CharField( max_length=60, verbose_name="Email")


    class Meta:
        """ Meta definition for Invoice. """
        verbose_name = "Livreur"
        verbose_name_plural = "Livreurs"

    def __str__(self):
        """ Unicode representation for Deliver """
        return "[{}] {} {}".format(self.pk, self.name, self.mail)
