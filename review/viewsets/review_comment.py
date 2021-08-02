from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,DestroyModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from mixins import CreateBySelfMixin
from permissions.is_owner_or_read_only import IsOwnerOrReadOnly
from ..models import ReviewComment
from ..serializers import ReviewCommentSerializer

class ReviewCommentViewSet(CreateBySelfMixin,GenericViewSet,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):

    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    
