from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django import forms
from .models import *


class ImageInline(GenericTabularInline):
    model = ImageGallery
    readonly_fields = ('image_url',)


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 30
    fields = (('title', 'slug'),
              ('category', 'production', 'collection'),
               'description', ('price', 'price_new'),
               'hits', 'stock', 'publicate', 'color', 'consist', 'weight', 'footage', 'stock_in', 'upload_xml')
    list_display = ('title', 'publicate', 'upload_xml', 'production', 'stock', 'price', 'created')
    list_editable = ('upload_xml', 'production', 'stock', 'price', 'publicate')
    list_filter = ('created', 'publicate', 'category', 'production')
    search_fields = ('title', 'production__title', 'color__title', 'consist__title')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInline, )

    def save_model(self, request, obj, form, change):
        """Отслеживаем обновленные поля"""
        update_fields = []
        if form.has_changed():
            update_fields = form.changed_data
        obj.update_fields = update_fields
        super().save_model(request, obj, form, change)


admin.site.register(ImageGallery)
admin.site.register(Product, ProductAdmin)

