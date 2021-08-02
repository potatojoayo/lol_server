from django_filters import rest_framework as filters
from ..models import Qna

class QnaFilter(filters.FilterSet):

    class Meta:
        model = Qna
        fields = {
            'user':['exact'],
            'product':['exact'],
            'qna_category':['exact'],
            'qna_status':['exact'],
            'written_date':['exact','range','lte','gte',],
            'update_date': ['exact','range','lte','gte'],
            'contents':['icontains']
        }
