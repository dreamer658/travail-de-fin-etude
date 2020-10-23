import requests
from moon.models.product import Product
from moon.models.customer import Customer
from moon.models.order import Order
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from moon.filters.filters import ProductFilter
from django.core.paginator import Paginator

def KidsProduct(request):
    """ All product of kids """

    kidsProducts = Product.objects.filter(gender__gender_name='Enfant')

    try:
    	 customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    if 'search' in request.GET:  # if there is searched term on the url
        search_term = request.GET['search']
        # getting the searched element in the url

        kidsProducts = kidsProducts.filter(name__icontains=search_term)

    #Search part, we'll get the info from the url bar and recreate the variable products with those information
    #So the variable products will be passed at template with the info we're searching


    #myFilter = ProductFilter(request.GET, queryset=products)
    #products = myFilter.qs

    paginated_products = Paginator(kidsProducts, 4)
    page_number = request.GET.get('page')
    product_page_obj = paginated_products.get_page(page_number)



    context = {'kidsProducts':product_page_obj, 'items': items, 'order': order, 'cartItems':cartItems}

    return render(request, 'kids.html', context)


def KidsShoes(request):
    """ List of Shoes. """


    listShoes=Product.objects.filter(productType__name='shoes', gender__gender_name='Enfant')
    try:
    	 customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    if 'search' in request.GET:  # if there is searched term on the url
        search_term = request.GET['search']
        # getting the searched element in the url

        listShoes = listShoes.filter(name__icontains=search_term)

    #Search part, we'll get the info from the url bar and recreate the variable products with those information
    #So the variable products will be passed at template with the info we're searching


    #myFilter = ProductFilter(request.GET, queryset=products)
    #products = myFilter.qs

    paginated_products = Paginator(listShoes, 4)
    page_number = request.GET.get('page')
    product_page_obj = paginated_products.get_page(page_number)

    context = {'listShoes':product_page_obj, 'items': items, 'order': order, 'cartItems':cartItems}

    return render(request, 'kidsShoes.html',context)

def KidsClothes(request):
    """ List of clothes. """

    listClothes=Product.objects.filter(productType__name='clothes', gender__gender_name='Enfant')

    try:
    	 customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    if 'search' in request.GET:  # if there is searched term on the url
        search_term = request.GET['search']
        # getting the searched element in the url

        listClothes = listClothes.filter(name__icontains=search_term)

    #Search part, we'll get the info from the url bar and recreate the variable products with those information
    #So the variable products will be passed at template with the info we're searching


    #myFilter = ProductFilter(request.GET, queryset=products)
    #products = myFilter.qs

    paginated_products = Paginator(listClothes, 4)
    page_number = request.GET.get('page')
    product_page_obj = paginated_products.get_page(page_number)



    context = {'listClothes':product_page_obj, 'items': items, 'order': order, 'cartItems':cartItems}

    return render(request, 'kidsClothes.html', context)

def KidsAccessory(request):
    """ List of Shoes. """

    listAccessory=Product.objects.filter(productType__name='accessory', gender__gender_name='Enfant')

    try:
    	 customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    if 'search' in request.GET:  # if there is searched term on the url
        search_term = request.GET['search']
        # getting the searched element in the url

        listAccessory = listAccessory.filter(name__icontains=search_term)

    #Search part, we'll get the info from the url bar and recreate the variable products with those information
    #So the variable products will be passed at template with the info we're searching


    #myFilter = ProductFilter(request.GET, queryset=products)
    #products = myFilter.qs

    paginated_products = Paginator(listAccessory, 4)
    page_number = request.GET.get('page')
    product_page_obj = paginated_products.get_page(page_number)

    context = {'listAccessory':product_page_obj, 'items': items, 'order': order, 'cartItems':cartItems}

    return render(request, 'kidsAccessory.html',
                  context)
