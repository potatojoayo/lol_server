from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from ..models import Size
from ..serializers import SizeSerializer
from ..filters import SizeFilter


class SizeViewSet(GenericViewSet,ListModelMixin):

    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    filterset_class = SizeFilter




