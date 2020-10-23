from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from moon.forms.userRegisterForm import UserRegisterForm
from django.contrib.auth.models import User
from moon.models.profile import UserProfile

def Register(request):
    """ The registration view """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            #username = request.POST['username']
            this_email = request.POST['email']
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            form.save()

            #ENVOI AUTOMATIQUE DU MAIL

            template = render_to_string('email.html',{'name': username})
            #user_form.username = user_form.cleaned_data.get('username')
            email = EmailMessage(
                'Bienvenue chez UrbanStreet !',
                template,
                'caldjango0@gmail.com',
                [this_email],
                )
            email.fail_silently=False
            email.send()
            messages.success(request, f'Compte pour {username} créé!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'userRegister.html',{'form':form})
