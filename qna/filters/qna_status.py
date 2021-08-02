from django_filters import rest_framework as filters
from ..models import QnaStatus

class QnaStatusFilter(filters.FilterSet):

    class Meta:
        model = QnaStatus
        fields = {
            'status':['iexact']
        }
