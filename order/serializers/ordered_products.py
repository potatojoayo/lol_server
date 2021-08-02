from rest_framework.serializers import ModelSerializer
from product.serializers import ProductSerializer
from ..models import OrderedProduct

class OrderedProductSerializer(ModelSerializer):

    ordered_product = ProductSerializer(source="product",read_only=True)

    class Meta:
        
        model = OrderedProduct
        fields = ['ordered_product','product', 'order','color','size','count']
