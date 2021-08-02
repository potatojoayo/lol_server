from django.db import models
from product.models import Product,Color,Size
from .order import Order

class OrderedProduct(models.Model):

    product = models.ForeignKey(Product,on_delete = models.RESTRICT) # id (int)
    order = models.ForeignKey(Order,on_delete=models.RESTRICT,blank=True, related_name='ordered_products') 
    color = models.ForeignKey(Color,on_delete=models.RESTRICT)
    size = models.ForeignKey(Size,on_delete=models.RESTRICT)
    count = models.IntegerField() 
    


