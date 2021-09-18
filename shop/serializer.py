from rest_framework import serializers

from .models import *


class ImageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageGallery
        fields = ('image',)


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', read_only=True, many=True)
    production = serializers.SlugRelatedField(slug_field='title', read_only=True)
    production_url = serializers.HyperlinkedIdentityField(view_name='shop:production_list', lookup_field='slug', read_only=True)
    images = ImageListSerializer(many=True)

    class Meta:
        model = Product
        exclude = ('publicate', 'created', 'updated', 'weight', 'footage', 'stock_in', 'color', 'consist', 'slug', 'upload_xml', 'hits', 'collection')
        extra_kwargs = {
            'url': {'view_name': 'shop:product_list_by_category', 'lookup_field': 'slug'},
        }


class CategoryListSerializer(serializers.Serializer):

    class Meta:
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageListSerializer(many=True)
    production = serializers.SlugRelatedField(slug_field='title', read_only=True)
    collection = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Product
        exclude = ('publicate', 'created', 'updated', 'category')