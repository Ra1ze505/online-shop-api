from django.urls import path
from .views import *


app_name = 'shop'

urlpatterns = [

    path('', Main.as_view(), name='shop'),
    path(r'<slug:slug>/', ProductsByCategory.as_view(), name='product_list_by_category'),
    path(r'production/<slug:slug>/', ProductionView.as_view(), name='production_list'),

]
