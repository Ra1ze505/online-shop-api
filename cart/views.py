from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Product
from .cart import Cart


class AddToCart(APIView):
    def post(self, request):
        cart = Cart(request)
        form_data = request.data
        product = get_object_or_404(Product, slug=form_data['product_slug'])
        if product:
            cart.add(product=product,
                     quantity=form_data['quantity'],
                     update_quantity=form_data['update'],
                     )
        return Response(status=201)


@api_view(('GET',))
def cart_remove(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.remove(product)
    return Response(status=200)


class CartView(APIView):
    def get(self, request):
        cart = Cart(request).cart
        for i in cart:
            try:
                cart[i]['image'] = 'http://' + request.get_host() + cart[i]['image']
            except KeyError:
                pass
        return Response(cart)


'''
{
"product_slug": "fibranatura-motochnaya-pryazha-papyrus-material-smesovka-svetlaya-pudra-229-05",
"quantity": 1,
"update": true
}

{
"product_slug": "test",
"quantity": 1,
"update": true
}
'''
