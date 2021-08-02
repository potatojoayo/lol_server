from django.db import models

class QnaCategory(models.Model):

    category = models.CharField(max_length=20)
