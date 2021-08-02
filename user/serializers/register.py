from .customer import CustomerSerializer
from django.contrib.auth import hashers
from ..models import Customer

class RegisterSerializer(CustomerSerializer):

    class Meta(CustomerSerializer.Meta):
        fields = ['email','password','name']
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self,validated_data):

        password = validated_data.pop('password')
        hashed_pwd = hashers.make_password(password)
        customer = Customer.objects.create(password=hashed_pwd, **validated_data)
        return customer 
        
    
