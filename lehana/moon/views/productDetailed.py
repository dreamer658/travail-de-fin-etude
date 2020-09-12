from moon.models.product import Product
from moon.models.customer import Customer
from moon.models.order import Order
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from moon.filters.filters import ProductFilter



def ProductDetailedView (request, pk):
    """ Display the details of a selected show based on its pk."""

    product = get_object_or_404(Product, pk=pk)
    try:
    	customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    context = {'product':product, 'items':items, 'order': order, 'cartItems':cartItems}

    return render(request, 'productDetailed.html', context)
