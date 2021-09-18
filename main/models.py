from django.db import models
from django.urls import reverse


class Container(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контейнер'
        verbose_name_plural = 'Контейнеры'


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка')
    container = models.ForeignKey(Container, blank=True, on_delete=models.CASCADE, verbose_name='Контейнер')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Production(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка')
    category = models.ManyToManyField('Category', blank=True, verbose_name='Категория', related_name='productions')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:production_view", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class CollectionForProduction(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Ссылка')
    production = models.ForeignKey(Production, blank=True, verbose_name='Производитель', related_name='collections', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:collection_view", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Колекция'
        verbose_name_plural = 'Колекции'


class Color(models.Model):
    title = models.CharField(max_length=50, verbose_name='Цвет')
    slug = models.SlugField(max_length=50, verbose_name='Ссылка', default='')
    code = models.CharField(max_length=7, verbose_name='Код цвета')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Сonsist(models.Model):
    title = models.CharField(max_length=50, verbose_name='Состав')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Составы'


class Status(models.Model):
    title = models.CharField(max_length=100, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = verbose_name + 'ы'

