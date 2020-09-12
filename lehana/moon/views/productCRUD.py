from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page

from moon.models.product import Product
from moon.forms.productForm import ProductForm
#from app.permissions.group import group_required


def CreateProduct(request):
    """Creating a Product

    This will allow creating a Product within our app, if we got permissions
    """

    form = ProductForm(request.POST or None)
    # when the user will click at save he will POST contents
    # if there is something in POST create a form with contents if not create an empty form (NONE)

    if form.is_valid():
        form.save()
        return redirect('home')  # nom de l'url qui correspond à la vue

    return render(request, 'crudProduct.html',
                  {'createProductForm': form})



def UpdateProduct(request, pk):
    """ Updating a location

    This will update a location within our app, if we got permissions
    """

    product = Product.objects.get(pk=pk)  # the slug we got on the url
    form = ProductForm(request.POST or None, instance=product)
    # it will allow us to modify filled with the instance of the "pk location"

    if form.is_valid():
        form.save()
        return redirect(product)
        # because of the model get_absolute_url I can access the view of this specific object.

    return render(request, 'crudProduct.html',
                  {'updateProductForm': form})



def DeleteProduct(request, pk):
    """Deleting a product

    This will delete a product within our app, if we got permissions
    """

    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        # if the user click on the submit button (displayed by the template)
        # he will post and confirm a delete.

        product.delete()
        #if product.genre == 'Femme':
        #return redirect('femme')
        return redirect('home')
    return render(request, 'crudProductDelete.html', {'product': product})
