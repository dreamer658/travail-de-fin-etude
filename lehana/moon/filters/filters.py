import django_filters

from moon.models.product import Product

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'name':['icontains'],

        }
