from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/cart/', include('cart.urls', namespace='cart')),
    path('api/v1/order/', include('orders.urls', namespace='order')),
    path('api/v1/', include('shop.urls', namespace='shop')),
    path('product/admin/', include('main.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

