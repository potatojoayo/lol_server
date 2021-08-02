from rest_framework import serializers
from ..models import Order,OrderedProduct
from .ordered_products import OrderedProductSerializer

class OrderSerializer(serializers.ModelSerializer):

    ordered_products = OrderedProductSerializer(many=True)

    class Meta:

        model = Order
        fields = '__all__'
        extra_kwargs = {'id':{'read_only':True},'user':{'read_only':True},'total_price':{'read_only':True},'status':{'read_only':True}} 

    def create(self,validated_data):

        ordered_products = validated_data.pop('ordered_products')
        order = Order.objects.create(**validated_data)
        for ordered_product in ordered_products:
            OrderedProduct.objects.create(order=order, **ordered_product)
        return order
        
    
