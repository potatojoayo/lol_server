from django_filters import rest_framework as filters
from ..models import QnaCategory

class QnaCategoryFilter(filters.FilterSet):

    class Meta:
        model = QnaCategory
        fields = {
            'category':['iexact']
        }
