from ..models import ReviewComment
from rest_framework import serializers

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = ['id','review','user','written_date', 'update_date','contents']
        extra_kwargs = {'user':{"read_only":True}}
