from rest_framework import routers
from django.urls import path, include
from .viewsets import OrderViewSet, OrderStatusViewSet

router = routers.DefaultRouter()
router.register('order', OrderViewSet, basename='order')
router.register('order_status', OrderStatusViewSet, basename='order_status')

urlpatterns = [
    path('',include(router.urls))
]
