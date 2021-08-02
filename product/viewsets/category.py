from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from ..models import Category
from ..serializers import CategorySerializer
from ..filters import CategoryFilter

class CategoryViewSet(GenericViewSet,ListModelMixin):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filtrset_class = CategoryFilter
