
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin
from rest_framework.decorators import api_view
from django.http import HttpResponse
from ..models import Product
from ..serializers import ProductSerializer
from ..filters import ProductFilter
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response



class ProductViewSet(GenericViewSet,RetrieveModelMixin,ListModelMixin):

    queryset = Product.objects.filter(display=True)
    filterset_class = ProductFilter 
    serializer_class = ProductSerializer
    response = HttpResponse("asd",content_type="text/plain")
    

    
@api_view(["GET"])
@ensure_csrf_cookie
def home(self, request):
    response = Response(None,status=None)
    response["Access-Control-Allow-Credentials"]=True;
    return Response(None, status = None)
  
    
    
