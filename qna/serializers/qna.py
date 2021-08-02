from rest_framework import serializers
from ..models import Qna
from .qna_comment import QnaCommentSerializer

class QnaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Qna 
        exclude = ['contents']
        extra_kwargs = {'user':{'read_only':True}}        
        
class QnaRetrieveSerializer(QnaSerializer):

    comments = QnaCommentSerializer(many=True,read_only=True)
    
    class Meta(QnaSerializer.Meta):
        
        exclude = []
        
