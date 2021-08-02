from django.db import models
from .review import Review

class Photo(models.Model):

   review = models.ForeignKey(Review,on_delete=models.CASCADE,related_name='photos',blank=True) 
   path = models.CharField(max_length=255)
   order = models.IntegerField()

   class Meta:
       ordering = ['order']
