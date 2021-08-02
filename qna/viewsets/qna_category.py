from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from ..models import QnaCategory
from ..serializers import QnaCategorySerializer 
from ..filters import QnaCategoryFilter

class QnaCategoryViewSet(GenericViewSet,ListModelMixin):

    queryset = QnaCategory.objects.all()
    serializer_class = QnaCategorySerializer
    filterset_class = QnaCategoryFilter
