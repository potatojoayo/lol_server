from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from ..models import OrderStatus
from ..serializers import OrderStatusSerializer

class OrderStatusViewSet(GenericViewSet,ListModelMixin):

    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    
