from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path(r'change-production/', views.admin_change_production),
    path(r'change-category/', views.admin_change_category),

]
