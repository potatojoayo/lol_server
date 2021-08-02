from django.db import models

class OrderStatus(models.Model):

    status = models.CharField(max_length=20)

    def __str__(self):

        return '{}'.format(self.status)
