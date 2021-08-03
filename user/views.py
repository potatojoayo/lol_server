from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers.login import LoginSerializer
from .serializers.customer import CustomerSerializer
from rest_framework.response import Response
from django.contrib.auth import login

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect
from rest_framework.decorators import api_view


class LoginView(APIView):

    permission_classes = [AllowAny] 

    
    @method_decorator(csrf_protect)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(CustomerSerializer(user).data)


