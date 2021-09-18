from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import *
from .models import *


@api_view(('GET',))
def admin_change_production(request):
    """Для ajax запроса на изменение производителя"""
    production_id = request.GET['production']
    collections = CollectionForProduction.objects.filter(production__id=production_id)
    serializer = CollectionSerialzer(collections, many=True)
    return Response(serializer.data)


@api_view(('GET',))
def admin_change_category(request):
    """Для ajax запроса на изменение категории"""
    categorys_id = dict(request.GET)
    ids = []
    for i in categorys_id['category[]']:
        ids.append(i)
    categorys = []
    fields = []
    for cat in ids:
        category = Category.objects.get(pk=cat)
        categorys.append(category.slug)
    for category in categorys:
        if category == 'motochnaya-pryazha':
            fields.extend(['color', 'consist', 'weight', 'footage', 'stock_in'])
        if category == 'pryazha-na-bobinah':
            for field in ('color', 'consist', 'weight', 'footage'):
                if field not in fields:
                    fields.extend([field])
        if category == 'mk' or 'gotovye-raboty':
            if 'color' not in fields:
                fields.extend(['color'])
    return Response(fields)
