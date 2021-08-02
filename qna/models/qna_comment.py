from django.db import models
from .qna import Qna
from user.models import User

class QnaComment(models.Model):

    qna = models.ForeignKey(Qna,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='qna_comments')
    written_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    contents = models.CharField(max_length=1000)

    def __str__(self):

        return '{}'.format(self.contents)
