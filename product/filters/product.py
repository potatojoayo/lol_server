from django_filters import rest_framework as filters
from ..models import Product

class ProductFilter(filters.FilterSet):

    class Meta:

        model = Product
        fields = {
            'name': ['icontains','iexact'],
            'price': ['gte','lte'],
            'soldout': ['exact'],
            'category': ['exact'],
            'brand': ['exact'],
            'colors': ['exact'],
            'sizes': ['exact'],
            'added_date': ['exact', 'range', 'gte', 'lte'],
        }
