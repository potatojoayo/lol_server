from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from ..models import QnaStatus
from ..serializers import QnaStatusSerializer
from ..filters import QnaStatusFilter

class QnaStatusViewSets(GenericViewSet,ListModelMixin):

    queryset = QnaStatus.objects.all()
    serializer_class = QnaStatusSerializer
    filterset_class = QnaStatusFilter
