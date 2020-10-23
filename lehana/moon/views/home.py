import requests
from moon.models.product import Product
from moon.models.customer import Customer
from moon.models.order import Order
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from moon.filters.filters import ProductFilter
from django.core.paginator import Paginator


def Home(request):
    """List of locations.

    This will display paginated list of locations and provide a search bar
    """

    products = Product.objects.all()
    product_page_obj = products[:4]
    product_four_last = products[4:8]

    try:
    	customer = request.user.customer

    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items



    context = {'items': items,
                'order': order, 'cartItems':cartItems,
                'products':product_page_obj,
                'product_four_last' : product_four_last}

    #context = {'products':products}

    return render(request, 'home.html', context)



def ResultsearchHome(request):
    """ The result of the search in the home page"""

    products = Product.objects.all()

    try:
    	customer = request.user.customer

    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items


    search_term = ''

    if 'search' in request.GET:  # if there is searched term on the url
        search_term = request.GET['search']
        # getting the searched element in the url

        products = products.filter(name__icontains=search_term)

    #Search part, we'll get the info from the url bar and recreate the variable products with those information
    #So the variable products will be passed at template with the info we're searching


    #myFilter = ProductFilter(request.GET, queryset=products)
    #products = myFilter.qs

    paginated_products = Paginator(products, 4)
    page_number = request.GET.get('page')
    product_page_obj = paginated_products.get_page(page_number)


    context = {'items': items,
                'order': order, 'cartItems':cartItems,
                'products':product_page_obj}

    #context = {'products':products}

    return render(request, 'resultsearchHome.html', context)



def Women(request):
    """Home views for women website"""

    return render(request, 'women.html', {})

def Kids(request):
    """Home views for kids website"""

    return render(request, 'kids.html', {})
