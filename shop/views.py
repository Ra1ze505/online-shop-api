from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from market import upload_in_product_xml, upload_image
from .serializer import *
from .service import ProductFilter, ProductionProductFilter


class Main(generics.ListAPIView):
    queryset = Product.objects.filter(publicate=True)
    serializer_class = ProductListSerializer


class ProductsByCategory(generics.ListAPIView):
    """Рендерим list или detail в зависимости от slug"""
    lookup_field = 'slug'
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        category = product = None
        self.category = self.product = False    # Для того, чтоб обращаться к этим аргументам в get_serializer()
        try:
            category = Category.objects.get(slug=self.kwargs['slug'])
        except ObjectDoesNotExist:
            try:
                product = Product.objects.filter(slug=self.kwargs['slug'], publicate=True)
            except ObjectDoesNotExist:
                return Product.objects.none()
        if category:
            self.category = True
            queryset = Product.objects.filter(category__slug=self.kwargs['slug'], publicate=True)
        else:
            self.product = True
            queryset = product
        return queryset

    def get_serializer(self, *args, **kwargs):
        if self.category:
            serializer_class = ProductListSerializer
        elif self.product:
            serializer_class = ProductDetailSerializer
        else:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class ProductionView(generics.ListAPIView):
    lookup_field = 'slug'
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductionProductFilter
    queryset = Product.objects.filter(publicate=True)


post_save.connect(upload_in_product_xml, sender=Product)
post_save.connect(upload_image, sender=ImageGallery)
