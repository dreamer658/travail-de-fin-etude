from moon.models.order import OrderItem, Order, ShippingAddress, Coupon
from moon.models.product import Product
from moon.models.customer import Customer
from moon.models.profile import Discount
from moon.forms.couponForm import CouponForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
import json
import datetime
import datetime
from django.utils import timezone
import random
import string


def get_random_string():
    """ To get an random string. """
    letters_and_digits = string.ascii_letters + string.digits
    res = ''.join((random.choice(letters_and_digits) for i in range(12)))
    print (res)
    return res


def Add_coupon():
    code = get_random_string()
    coupon = Coupon(code=code)
    coupon.save()



def Verifycoupon(request):
    """ View to verify the promo code entered by the user """

    bool = False
    coupons = Coupon.objects.all()
    form = CouponForm(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data['post']
        form.save()
    if product.favourites.filter(pk=request.user.pk).exists():
        pass

    context = {'couponform':form}
    return render (request, 'cart.html', context)



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

    """ COUPON PROMO CODE PART """

    bool = False
    coupons = Coupon.objects.all()
    form = CouponForm(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data['code']

        try:
            coupon = Coupon.objects.get(code__iexact=code, active=True)
            bool = True
            #request.user.userprofile.got_a_discount = False
            #Once the user enter the code his attribute got_a_discount becomes False until he'll get another discount.


        except Coupon.DoesNotExist:
            pass
        if request.user.is_authenticated:
            if bool==True and request.user.userprofile.got_a_discount == True:
                request.user.userprofile.got_a_discount=False
                #Once the user enter the code his attribute "got_a_discount" becomes False until he'll get another discount.
                messages.success(request, f"T'as maintenant une reduction de 20% sur l'ensemble de ta commande ;)")
                order.been_discounted = True
                request.user.userprofile.save()
                order.save()
                print("NEW ORDER TOTAL", order.get_cart_total)
            else:
                messages.warning(request, f"Ah dommage c'est pas le bon code, pour toi.")
        else:
            messages.warning(request, f"Ah dommage c'est pas le bon code, pour toi.")
        return redirect('Cart')

    context = { 'couponform':form, 'items': items, 'order': order, 'cartItems':cartItems}

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
    product = get_object_or_404(Product, pk=productId)
    print ("product:", product.name, "stock:", product.stock)

    try:
    	customer = request.user.customer
    except:
    	device = request.COOKIES['device']
    	customer, created = Customer.objects.get_or_create(device=device)

    #product = Product.objects.get(pk=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if product.stock > 0:
        if action == 'add' and orderItem.quantity < product.stock:
            messages.success(request, f"Ajouté au panier")
            orderItem.quantity = (orderItem.quantity + 1)
            print('jaime les chats')
        elif action == 'add' and orderItem.quantity >= product.stock:
            print("quantité depasse le stock pour:", product.name)
            messages.warning(request, f"Votre panier possède le stock restant pour cet article")
    else:
        print(product.name, "Stock non disponible")
        messages.warning(request, f"Cet article n'est plus disponible, il le sera bienôt ;)")

    if action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    if action == 'delete':
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
        order.complete = True #this is the statut of an order the attribut complete of product becomes True
        for item in items: #For all the item in the cart I'll decrement each of them once payed.
            item.product.stock -= item.quantity
            item.product.save()
        if request.user.is_authenticated : #I'm incrementing dicount attribut in user profil to give a promo to user.
            userGender = request.user.userprofile.gender
            request.user.userprofile.discount_rate += 1
            request.user.userprofile.save()

            if request.user.userprofile.discount_rate >= 2: #Discount code part
                request.user.userprofile.got_a_discount = True
                template = render_to_string('promocode.html',{'name': request.user.username})
                #user_form.username = user_form.cleaned_data.get('username')
                email = EmailMessage(
                    'Sujet:Félicitations, ton code promo !',
                    template,
                    'caldjango0@gmail.com',
                    [request.user.email],
                    )
                email.fail_silently=False
                email.send()

                request.user.userprofile.discount_rate = 0
                request.user.userprofile.save()
                Add_coupon() #Adding a new coupon on the coupon table.
    order.been_discounted = False
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



    context = {'items': items, 'order': order, 'cartItems':cartItems}

    return render(request, 'cart.html', context)
