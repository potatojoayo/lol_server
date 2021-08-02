from ..models import Photo
from rest_framework import serializers

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo 
        fields = ['id','review','path','order']
