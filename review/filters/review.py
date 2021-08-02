from django_filters import rest_framework as filters
from ..models import Review 

class ReviewFilter(filters.FilterSet):

    class Meta:

        model = Review 
        fields = {
            'user': ['exact'],
            'product': ['exact'],
            'written_date': ['exact','date__gte','date__lte', 'range'],
            'update_date': ['exact','date__gte','date__lte', 'range'],
            'contents': ['icontains', 'iexact'],
        }
