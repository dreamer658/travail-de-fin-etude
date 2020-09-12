from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from moon.forms.userRegisterForm import UserRegisterForm
from django.contrib.auth.models import User

def Register(request):
    """ The registration view """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            #username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            username = form.cleaned_data.get('username')


            #user=User.objects.create_user(username=username, email=email)
            #user.set_password(password)
            #user.is_active = False
            #user.save()
            #template = render_to_string('email.html',{'name':user.username})
            #email = EmailMessage(
            #    'Sujet:Cimer cousin !',
            #    template,
            ##    'caldjango0@gmail.com',
            #    [user.email],
            #    )
            #email.fail_silently=False
            #email.send() 
            form.save()
            messages.success(request, f'Compte pour {username} créé!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'userRegister.html',{'form':form})
