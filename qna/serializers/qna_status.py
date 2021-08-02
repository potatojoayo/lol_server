from ..models import QnaStatus
from rest_framework import serializers

class QnaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnaStatus 
        fields = ['id','status']

