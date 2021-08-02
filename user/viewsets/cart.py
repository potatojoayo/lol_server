from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from mixins import PossessionQuerySetMixin,CreateBySelfMixin
from permissions import IsSelf
from ..models import Cart
from ..serializers import CartSerializer

class CartViewSet(PossessionQuerySetMixin,CreateBySelfMixin,ModelViewSet):

    model = Cart
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated,IsSelf]
