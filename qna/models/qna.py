from django.db import models
from .qna_category import QnaCategory
from .qna_status import QnaStatus
from product.models import Product
from user.models import User

class Qna(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='qnas')
    product = models.ForeignKey(Product,on_delete=models.RESTRICT,related_name='qnas')
    qna_category = models.ForeignKey(QnaCategory,on_delete=models.RESTRICT,related_name='qnas')
    qna_status = models.ForeignKey(QnaStatus,on_delete=models.RESTRICT,related_name='qnas')
    title = models.CharField(max_length=100,default='')
    written_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    contents = models.CharField(max_length=1000)
    is_secret = models.BooleanField(default=False)
