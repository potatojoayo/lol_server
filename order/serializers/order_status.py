from ..models import OrderStatus
from rest_framework import serializers

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['status']
