from rest_framework.viewsets import ModelViewSet
from permissions import IsOwnerOrReadOnly,CreateUserOnly
from mixins import CreateBySelfMixin
from ..models import Review
from ..serializers import ReviewSerializer,ReviewRetrieveSerializer
from ..filters import ReviewFilter

class ReviewViewSet(CreateBySelfMixin,ModelViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter
    permission_classes = [IsOwnerOrReadOnly,CreateUserOnly]

    
    def get_serializer_class(self):

        if self.action == 'list':
            return ReviewSerializer
        else:
            return ReviewRetrieveSerializer
