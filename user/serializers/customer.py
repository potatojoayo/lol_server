from ..models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {'password':{'write_only':True}}

