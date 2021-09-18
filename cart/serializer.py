from rest_framework import serializers

from .cart import Cart



class CartListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

