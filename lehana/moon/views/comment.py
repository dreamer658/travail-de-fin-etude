from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from moon.forms.comForm import ComForm
from moon.models.product import Product
from moon.models.profile import Comment


@login_required
def CommentView(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comment = Comment.objects.filter(product=pk) #To display only the coms with that pk
    a_user = request.user
    com = Comment(product=product, user=a_user)
    form = ComForm(request.POST or None, instance=com)
    if form.is_valid():
        form.save()
        return redirect('avis', pk=pk) #name of the url of this view

    return render (request, 'comTemp.html', {'form':form})


@login_required
def ReviewProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comment = Comment.objects.filter(product=pk) #To display only the coms with that pk

    return render (request, 'avis.html', {'comment':comment, 'product':product})
