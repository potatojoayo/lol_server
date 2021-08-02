from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from ..models import Brand
from ..serializers import BrandSerializer
from ..filters import BrandFilter


class BrandViewSet(GenericViewSet,ListModelMixin):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filterset_class = BrandFilter


