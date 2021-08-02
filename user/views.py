from django.contrib.auth.views import LoginView as PreLoginView
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt
class LoginView(PreLoginView): 

    pass



