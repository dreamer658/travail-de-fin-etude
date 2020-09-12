from django import forms
from moon.models.product import Product

class ProductForm(forms.ModelForm):
    """ Location form """

    """Meta class for the ProductForm"""
    class Meta:
        model = Product
        fields = ['maker', 'gender','name','stock','price','image','color','material','description']
