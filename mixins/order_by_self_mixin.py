import datetime
from order.models import OrderStatus
from product.models import Product

class OrderBySelfMixin:

    def perform_create(self,serializer):
        
        order_status = OrderStatus.objects.get(id=1)
        id = self.generate_order_id()
        total_price = 0
        products = self.request.data['ordered_products']
        for product in products:
            product_id = product['product']
            total_price += Product.objects.get(id=product_id).price
        serializer.save(id=id,user=self.request.user,total_price=total_price,status=order_status)

    #날짜8자+시간6자+신원(userId modulo 10000)4자 => 18자
    def generate_order_id(self):

        date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        order_id = self.request.user.id%10000
        return date + format(order_id,'04')
