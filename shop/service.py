from django_filters import rest_framework as filters

from .models import Product


class CharFieldinFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['price', 'production']


class ProductionProductFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['price', 'production__collections']


