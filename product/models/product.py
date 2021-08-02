from django.db import models
from .brand import Brand
from .category import Category
from .color import Color
from .size import Size

class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length = 255)
    pia = models.TextField()
    soldout = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.RESTRICT)
    brand = models.ForeignKey(Brand,on_delete=models.RESTRICT)
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    added_date = models.DateField(auto_now_add=True) 
    display = models.BooleanField(default=True)

    def __str__(self):

        return '{}'.format(self.name)
