from django.db import models

class QnaStatus(models.Model):

    status = models.CharField(max_length=20)
