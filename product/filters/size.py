from django_filters import rest_framework as filters
from ..models import Size 

class SizeFilter(filters.FilterSet):

    class Meta:

        model = Size 
        fields = {
            'size': ['iexact']
        }
