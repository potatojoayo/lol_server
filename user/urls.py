from rest_framework import routers
from django.urls import path, include
from .viewsets import AddressViewSet, CartViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register('address', AddressViewSet, basename='address')
router.register('cart', CartViewSet, basename='cart')
router.register('customer', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
]
