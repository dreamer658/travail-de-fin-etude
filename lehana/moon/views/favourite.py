from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
#from django.http import HttpResponse
from django.template import loader
from moon.models.product import Product
#from moon.models.customer import Customer
#from moon.models.order import Order
from moon.filters.filters import ProductFilter


@login_required
def Favourite(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # IF the user click on the heart: if the product is already on favorite then remove that product from the favourite
    # ELSE : if the product is not already in the favorites then add it the favorite
    if product.favourites.filter(pk=request.user.pk).exists():
        product.favourites.remove(request.user)
        product.is_liked=False
        product.save()


    else:
        product.favourites.add(request.user)
        product.is_liked=True
        product.save()
        messages.success(request, f'Ajouter au favoris !')


    #return redirect('home')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def FavouriteList(request):
    #if we find a product that has a favourite field that equals user.pk we gonna return that post
    new = Product.objects.filter(favourites=request.user)
    return render (request,'favourites.html', {'new':new})
