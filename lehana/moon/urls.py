from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from moon.views import views
from moon.views.productDetailed import ProductDetailedView
from moon.views.men import MenShoes, MenClothes, MenAccessory
from moon.views.cart import Cart, Commander, UpdateItem, ProcessOrder,ProdDetailTest
from moon.views.authentication import Register
from moon.views.userprofileView import UserProfileView
from moon.views.comment import CommentView, ReviewProduct
from moon.views.favourite import Favourite, FavouriteList
from moon.views.productCRUD import CreateProduct, UpdateProduct, DeleteProduct
from moon.views.deleteComment import DeleteComment

urlpatterns = [
    # Home page

    url(r'^$', views.home, name='home'),

    #products
    url(r'^productdetailTest/(?P<pk>[0-9]+)$', ProdDetailTest,name='ProdDetailTest'),
    url(r'^product/detail/(?P<pk>[0-9]+)$', ProductDetailedView,name='ProductDetailed'),
    #products crud
    url(r'^product/create/$', CreateProduct, name='createproduct'),
    url(r'^product/update/(?P<pk>[0-9]+)/?$', UpdateProduct, name='updateproduct'),
    url(r'^product/delete/(?P<pk>[0-9]+)/?$', DeleteProduct,name='deleteproduct'),

    #MEN
    url(r'^men/$',views.men,name='Men'),
    url(r'^men/shoes/$', MenShoes,name='MenShoes'),
    url(r'^men/clothes/$', MenClothes,name='MenClothes'),
    url(r'^men/accessories/$', MenAccessory,name='MenAccessory'),
    #Women
    url(r'^women/$', views.women,name='Women'),
    #Kids
    url(r'^kids/$', views.kids,name='Kids'),
    #cart
    url(r'^cart/$', Cart,name='Cart'),
    url(r'^checkout/$', Commander, name='Commander'),
    url(r'^updateItem/$', UpdateItem, name='updateItem'),
    url(r'^process_order/$', ProcessOrder, name='process_order'),

    #authentication
    url(r'^register/$', Register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    #userProfile
    url(r'^profile/$', UserProfileView, name='userProfile'),

    #Reset password Check this on django doc
    url(r'^password/reset/$',
        auth_views.PasswordResetView.as_view(
        template_name='passwordResetForm.html'
        ),name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    #Comments
    url(r'^avis/(?P<pk>[0-9]+)/$', ReviewProduct,name='avis'),
    url(r'^commentaire/(?P<pk>[0-9]+)/$', CommentView,name='commentView'),
    #Comment delete
    url(r'^comment/delete/(?P<pk>[0-9]+)/?$', DeleteComment,name='deletecomment'),

    #Likes
    url(r'^favoris/(?P<pk>[0-9]+)$', Favourite,name='favourite'),
    url(r'^favorisList$', FavouriteList,name='favouriteList'),


]
