from django_filters import rest_framework as filters
from ..models import Color

class ColorFilter(filters.FilterSet):

    class Meta:

        model = Color 
        fields = {
            'color': ['icontains','iexact'],
        }
