from django.db import models
from product.models import Product
from user.models import User

class Review(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    product = models.ForeignKey(Product,on_delete=models.RESTRICT,related_name='reviews')
    written_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    contents = models.CharField(max_length=255)
    

