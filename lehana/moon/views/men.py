from moon.models.product import Product
from django.shortcuts import render
from django.http import HttpResponse

def MenShoes(request):
    """ List of Shoes. """


    products = Product.objects.filter(gender__gender_name='Homme')
    listShoes = []
    for i in products: # This test if an object on the queryset list "products" has un héritier "Shoes".
        if hasattr(i, 'shoes'):
            listShoes.append(i)

    return render(request, 'menShoes.html',
                  {'listShoes': listShoes})

def MenClothes(request):
    """ List of Shoes. """


    products = Product.objects.filter(gender__gender_name='Homme')
    listClothes = []
    for i in products: # This test if an object on the queryset list "products" has un héritier "Shoes".
        if hasattr(i, 'clothes'):
            listClothes.append(i)

    return render(request, 'menClothes.html',
                  {'listClothes': listClothes})

def MenAccessory(request):
    """ List of Shoes. """


    products = Product.objects.filter(gender__gender_name='Homme')
    listAccessory = []
    for i in products: # This test if an object on the queryset list "products" has un héritier "Shoes".
        if hasattr(i, 'accessory'):
            listAccessory.append(i)

    return render(request, 'menAccessory.html',
                  {'listAccessory': listAccessory})
