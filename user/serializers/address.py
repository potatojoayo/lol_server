from ..models import Address 
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Address
        fields = ['id','reciever','phone','address1', 'address2','zip_code','shipment_memo','user']
        extra_kwargs = {'user':{'read_only':True}}

