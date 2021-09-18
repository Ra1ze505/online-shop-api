from django.contrib import admin
from .models import *


class MainAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryInLine(admin.TabularInline):
    model = Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (CategoryInLine,)


admin.site.register(Production, MainAdmin)
admin.site.register(Color, MainAdmin)
admin.site.register(Сonsist)
admin.site.register(Status)
admin.site.register(CollectionForProduction, MainAdmin)
