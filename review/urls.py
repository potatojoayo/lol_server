from rest_framework import routers
from django.urls import path, include
from .viewsets import ReviewViewSet, ReviewCommentViewSet 

router = routers.DefaultRouter()
router.register('review', ReviewViewSet, basename='review')
router.register('review_comment', ReviewCommentViewSet, basename='review_comment')

urlpatterns = [
    path('',include(router.urls))
]
