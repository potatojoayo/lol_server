from django.db import models
from user.models import User
from .order_status import OrderStatus

class Order(models.Model):

    id = models.CharField(primary_key=True, max_length=18)
    user = models.ForeignKey(User,on_delete = models.SET_NULL,null=True,related_name='orders')
    status = models.ForeignKey(OrderStatus,on_delete = models.RESTRICT,related_name='orders')
    total_price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    shipment_memo = models.CharField(max_length=50,null=True,blank=True) 


