from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from ..models import Color
from ..serializers import ColorSerializer
from ..filters import ColorFilter


class ColorViewSet(GenericViewSet,ListModelMixin):

    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filterset_class = ColorFilter
