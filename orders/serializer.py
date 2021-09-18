from rest_framework import serializers

from .models import *

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ('paid', 'total_price', 'url_pay', 'status')