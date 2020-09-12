from django.shortcuts import render, redirect, get_object_or_404
from moon.models.profile import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def UserProfileView(request):
    """ The view for the profile user """
    user = request.user
    print(user)
    if user.is_authenticated:
        userProfile = UserProfile.objects.get(user=user)

    return render(request, 'userProfile.html',{'userProfile':userProfile})
