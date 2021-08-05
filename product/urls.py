from .viewsets import ProductViewSet,CategoryViewSet,BrandViewSet,ColorViewSet,SizeViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter() 

router.register('product',ProductViewSet,basename='product')
router.register('brand',BrandViewSet,basename='brand')
router.register('category',CategoryViewSet,basename='category')
router.register('color',ColorViewSet,basename='color')
router.register('size',SizeViewSet,basename='size')

urlpatterns = [
    path('', include(router.urls)),
]

