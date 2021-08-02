from ..models import QnaCategory
from rest_framework import serializers

class QnaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QnaCategory
        fields = ['id','category']

