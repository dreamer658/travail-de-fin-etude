from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from moon.models.order import OrderItem, Order, ShippingAddress
from moon.models.product import Product
from django.contrib.auth.decorators import login_required

@login_required
def DiscountView(request):

    try:
    	 customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    #promos = Discount.objects.filter(user=request.user)
    promos = Product.objects.filter(discountUser=request.user)
    context = {'items': items, 'order': order, 'cartItems':cartItems, 'promos':promos}


    return render(request, 'discount.html', context)
