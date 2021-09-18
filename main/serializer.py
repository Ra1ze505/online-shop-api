from rest_framework import serializers

from .models import *


class CollectionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CollectionForProduction
        fields = ('title', 'id')
