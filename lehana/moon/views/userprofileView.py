from django.shortcuts import render, redirect, get_object_or_404
from moon.models.profile import UserProfile
from moon.models.order import Order
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def UserProfileView(request):
    """ The view for the profile user """
    user = request.user
    print(user)
    if user.is_authenticated:
        userProfile = UserProfile.objects.get(user=user)
        userOrder = Order.objects.filter(customer__user=user)
    context={'userProfile':userProfile, 'userOrder':userOrder}

    return render(request, 'userProfile.html',context)

@login_required
def UserOrderView(request):
    """ The view for the user Order """
    user = request.user
    print(user)
    if user.is_authenticated:
        userOrder = Order.objects.filter(customer__user=user)

    print(userOrder)
    return render(request, 'userProfile.html',{'userOrder':userOrder})
