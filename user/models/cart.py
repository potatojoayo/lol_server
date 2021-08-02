from django.db import models
from product.models import Product,Color,Size
from .user import User 

class Cart(models.Model):

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete = models.RESTRICT)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.RESTRICT)
    size = models.ForeignKey(Size,on_delete=models.RESTRICT)
    count = models.IntegerField()
