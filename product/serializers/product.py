from rest_framework import serializers
from ..models import Product
from ..serializers import ImageSerializer

class ProductSerializer(serializers.ModelSerializer):
    
    images = ImageSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        




