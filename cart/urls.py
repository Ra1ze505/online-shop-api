from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path(r'', CartView.as_view(), name='cart_detail'),
    path(r'add/', AddToCart.as_view(), name='cart_add'),
    path(r'remove/<slug:slug>/', cart_remove, name='cart_remove'),
]
