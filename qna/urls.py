from rest_framework import routers
from django.urls import path, include
from .viewsets import QnaViewSet, QnaStatusViewSets, QnaCommentViewSet, QnaCategoryViewSet 

router = routers.DefaultRouter()
router.register('qna', QnaViewSet, basename='qna')
router.register('qna_status', QnaStatusViewSets, basename='qna_status')
router.register('qna_comment', QnaCommentViewSet, basename='qna_comment')
router.register('qna_category', QnaCategoryViewSet, basename='qna_category')

urlpatterns = [
    path('',include(router.urls))
]
