from django.db import models
from .product import Product

class Image(models.Model):

    id= models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.RESTRICT,related_name='images')
    path = models.CharField(max_length=255)
    order = models.IntegerField()

    class Meta:
        unique_together = ['product','path']
        ordering = ['order']
