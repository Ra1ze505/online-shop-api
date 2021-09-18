from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from main.models import Category, Container, Color, Production, Сonsist, CollectionForProduction


class ImageGallery(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    image = models.ImageField(upload_to='products/%Y/%m/%d')

    def get_src(self):
        return self.image.url

    def __str__(self):
        return f'Изображения для {self.content_object}'

    def image_url(self):
        return mark_safe(f'<img src="{self.image.url}" width="auto" height="200px"')

    class Meta:
        verbose_name = 'Галерея изображений'
        verbose_name_plural = 'Галерея изображений'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Ссылка')
    category = models.ManyToManyField(Category, verbose_name='Категория')
    production = models.ForeignKey(Production, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name='Производитель')
    collection = models.ForeignKey(CollectionForProduction, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name='Коллекция')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    price_new = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Новая цена', blank=True, default=0)
    stock = models.PositiveIntegerField(verbose_name='В наличии')
    hits = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True, verbose_name='Рейтинг')
    publicate = models.BooleanField(verbose_name='Публикация', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    images = GenericRelation('imagegallery')
    color = models.ForeignKey(Color, verbose_name='Цвет', on_delete=models.CASCADE, blank=True, null=True)
    consist = models.ForeignKey(Сonsist, verbose_name='Состав', blank=True, null=True, on_delete=models.CASCADE)
    weight = models.IntegerField(verbose_name='Вес, гр', blank=True, null=True)
    footage = models.CharField(max_length=50, verbose_name='Метраж', blank=True, null=True)
    stock_in = models.IntegerField(verbose_name='Количество в упаковке, шт', blank=True, null=True)
    upload_xml = models.BooleanField(verbose_name='Выгрузить на Я.Маркет', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

    class Meta:
        ordering = ('-hits',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
