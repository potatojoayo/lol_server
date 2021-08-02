from ..models import QnaComment
from rest_framework import serializers

class QnaCommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = QnaComment
        fields = ['id','qna','user','written_date','update_date','contents']
        extra_kwargs={'user':{'read_only':True}}
    
