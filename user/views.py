from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers.login import LoginSerializer
from .serializers.customer import CustomerSerializer
from rest_framework.response import Response
from django.contrib.auth import login

class LoginView(APIView):

    permission_classes = (AllowAny,) 

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(CustomerSerializer(user).data)


