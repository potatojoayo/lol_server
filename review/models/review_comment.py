from django.db import models
from .review import Review
from user.models import User

class ReviewComment(models.Model):

    review = models.ForeignKey(Review,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    written_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    contents = models.CharField(max_length=200)
    
