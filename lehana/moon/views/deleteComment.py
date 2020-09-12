from django.shortcuts import render, redirect
from django.urls import reverse
#from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect
from moon.models.product import Product
from moon.models.profile import Comment
from moon.forms.productForm import ProductForm
#from app.permissions.group import group_required


def DeleteComment(request, pk):
    """Deleting a product

    This will delete a product within our app, if we got permissions
    """
    comment = Comment.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        # if the user click on the submit button (displayed by the template)
        # he will post and confirm a delete.

        comment.delete()
        return redirect('home')
    return render(request, 'deleteComment.html', {'comment': comment, 'user':user})
