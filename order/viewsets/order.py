from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from permissions import IsSelf
from mixins import PossessionQuerySetMixin,OrderBySelfMixin
from ..models import Order
from ..serializers import OrderSerializer
from ..filters import OrderFilter

class OrderViewSet(PossessionQuerySetMixin,OrderBySelfMixin,GenericViewSet,ListModelMixin,CreateModelMixin):

    model = Order
    serializer_class = OrderSerializer 
    filterset_class = OrderFilter
    permission_classes = [IsAuthenticated,IsSelf]
    

