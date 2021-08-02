from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,DestroyModelMixin 
from rest_framework.permissions import IsAuthenticated
from mixins import CreateBySelfMixin
from permissions.is_owner_or_read_only import IsOwnerOrReadOnly
from ..models import QnaComment
from ..serializers import QnaCommentSerializer

class QnaCommentViewSet(CreateBySelfMixin,GenericViewSet,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):

    queryset = QnaComment.objects.all()
    serializer_class = QnaCommentSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
