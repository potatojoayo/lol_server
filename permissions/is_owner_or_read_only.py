from rest_framework import permissions
from qna.models import Qna

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):

        if request.method in permissions.SAFE_METHODS:      
            if isinstance(obj,Qna):
               return obj.user == request.user or not obj.is_secret
            return True
        return obj.user == request.user
