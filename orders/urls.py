from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path(r'create/', views.OrderCreate.as_view(), name='create'),
]
