from cart.cart import Cart
from .serializer import *
from rest_framework import generics


class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        cart = Cart(self.request)
        id_by_order = serializer.save(total_price=cart.get_total_price()).id
        for item in cart:
            pr = Product.objects.get(id=item['product'].id)
            pr.stock -= item['quantity']
            pr.save()
            OrderItem.objects.create(order=Order.objects.get(id=id_by_order),
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'],
                                     )
        cart.clear()



"""
{
    "first_name": "Andrey",
    "last_name": "Matveev",
    "email": "test@mail.ru",
    "phone": "89295115246",
    "delivery": "S",
    "address_PVZ": "dsaefgswegse",
    "address": "dsgsrggsrf",
    "postal_code": "123456",
    "city": "Moscow",
    "region": "Moscow",
    "paid": true
}
"""
