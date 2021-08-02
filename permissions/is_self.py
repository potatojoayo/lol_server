from rest_framework.permissions import BasePermission
from user.models import User

class IsSelf(BasePermission):

    def has_object_permission(self,request,view,obj):

        customer = request.user 

        if customer.is_admin:
            return True

        if isinstance(obj,User):
            return customer == obj

        return customer == obj.user
