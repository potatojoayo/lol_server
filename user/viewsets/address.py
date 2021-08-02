from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated
from mixins import PossessionQuerySetMixin,CreateBySelfMixin
from permissions import IsSelf
from ..models import Address 
from ..serializers import AddressSerializer

class AddressViewSet(PossessionQuerySetMixin,CreateBySelfMixin,ModelViewSet):

    model = Address
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated,IsSelf]
