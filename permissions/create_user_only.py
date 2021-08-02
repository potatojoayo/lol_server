from rest_framework.permissions import IsAuthenticated

class CreateUserOnly(IsAuthenticated):

    def has_permission(self,request,view):

        if request.method == 'POST':
            return super().has_permission(request,view)
        else:
            return True
        
