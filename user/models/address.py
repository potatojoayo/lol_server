from django.db import models
from .user import User

class Address(models.Model):

    reciever = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    shipment_memo = models.CharField(max_length=200,null=True,blank=True)
    user= models.ForeignKey(User,on_delete = models.CASCADE,related_name='addresses')
    
