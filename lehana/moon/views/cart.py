from moon.models.order import OrderItem, Order, ShippingAddress
from moon.models.product import Product
from moon.models.customer import Customer
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
import datetime


def Cart(request):

    # TOUS CE BLOCK LIGNE 14 A 27 EST (peut-etre sauf ligne 22) est necessaire à l'affichage du nb d'elem dans le panier.
    try:
    	customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    context = {'items': items, 'order': order, 'cartItems':cartItems}

    return render(request, 'cart.html', context)


def Commander(request):
    """ View of the checkout. """

    try:
    	customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

    context = {'items': items, 'order': order, 'cartItems':cartItems}

    return render(request, 'commander.html', context)


#We're reciving data from cart.js and in js we're reciving the data from the template.
def UpdateItem(request):

    #Here we loading all those info in cart.js
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    try:
    	customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    product = Product.objects.get(pk=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Article ajouté ma douce', safe=False)


def ProcessOrder(request):

    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    try:
    	customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    total = float(data['form']['Total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total :
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer = customer,
        order = order,
        locality = data['shipping']['locality'],
        street = data['shipping']['street'],
        street_number = data['shipping']['street_number'],
        postal_code = data['shipping']['postal_code'],
        city = data['shipping']['city'],
    )


    return JsonResponse('Payment submitted..', safe=False)



def ProdDetailTest(request, pk):

    #product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        #product = Product.objects.get(pk=pk)
        product = get_object_or_404(Product, pk=pk)
        #Get user account information

        try:
        	customer = request.user.customer
        except:
        	device = request.COOKIES['device'] #grabbing the cookie we called device on the frontend
        	customer, created = Customer.objects.get_or_create(device=device)


        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        #orderItem.quantity=request.POST['quantity']
        #orderItem.save()
        return redirect('Cart')

    else:
        try:
        	customer = request.user.customer
        except:
        	device = request.COOKIES['device'] #grabbing the cookie we called device on the frontend
        	customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    context = {'product':product,'items':items,'cartItems':cartItems}
    return render(request, 'prod_detail_test.html', context)
