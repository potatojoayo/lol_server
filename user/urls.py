from rest_framework import routers
from django.urls import path, include
from .viewsets import  AddressViewSet, CartViewSet, CustomerViewSet
from .views import LoginView

router = routers.DefaultRouter()
router.register('address', AddressViewSet, basename='address')
router.register('cart', CartViewSet, basename='cart')
router.register('customer', CustomerViewSet, basename='customer')

urlpatterns = [ 
    path('', include(router.urls)) ,
    path('login/', LoginView.as_view())
]

