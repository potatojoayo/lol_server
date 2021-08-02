from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from django.contrib.auth.models import AnonymousUser
from mixins import CreateBySelfMixin
from ..models import Qna
from ..serializers import QnaSerializer,QnaRetrieveSerializer
from ..filters import QnaFilter
from permissions import IsOwnerOrReadOnly,CreateUserOnly

class QnaViewSet(CreateBySelfMixin,ModelViewSet):

    serializer_class = QnaSerializer
    filterset_class = QnaFilter
    permission_classes = [IsOwnerOrReadOnly,CreateUserOnly]
    queryset = Qna.objects.all()

    def get_serializer_class(self):

        if self.action == 'retrieve':
           return QnaRetrieveSerializer
        else:
            return QnaSerializer
