from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser
from .models import Customer

class IsNotLoggedIn(BasePermission):

    def has_permission(self,request,view):

       print(isinstance(request.user,AnonymousUser))
       return isinstance(request.user,AnonymousUser)
