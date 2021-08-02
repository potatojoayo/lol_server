from django_filters import rest_framework as filters
from ..models import Photo

class PhotoFilter(filters.FilterSet):

    class Meta:

        model = Photo
        fields = {
            'review': ['exact'],
            'path': ['icontains', 'iexact'], 
            'order': ['exact','gte','lte']
        }
