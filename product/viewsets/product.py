
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin
from rest_framework.decorators import api_view
from django.http import HttpResponse
from ..models import Product
from ..serializers import ProductSerializer
from ..filters import ProductFilter
from django.utils.decorators import method_decorator


class ProductViewSet(GenericViewSet,RetrieveModelMixin,ListModelMixin):

    queryset = Product.objects.filter(display=True)
    filterset_class = ProductFilter 
    serializer_class = ProductSerializer
    response = HttpResponse("asd",content_type="text/plain")

    
    
