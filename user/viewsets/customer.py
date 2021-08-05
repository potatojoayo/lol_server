from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsNotLoggedIn
from permissions import IsSelf
from mixins import PossessionQuerySetMixin
from ..models import Customer
from ..serializers import RegisterSerializer, CustomerSerializer


class CustomerViewSet(PossessionQuerySetMixin, GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):

    model = Customer

    def get_serializer_class(self):

        if self.action == 'create':
            return RegisterSerializer
        return CustomerSerializer

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [IsNotLoggedIn]
        else:
            permission_classes = [IsAuthenticated, IsSelf]
        return [permission() for permission in permission_classes]
