from django.conf import settings
from django.contrib.auth.models import Permission, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from .user import User

class CustomerManager(BaseUserManager):

    def register(self,email,name,password=None):
        customer = self.model(
            email = self.normalize_email(email),
            name = name
        )
        customer.set_password(password)
        customer.save(using=self._db)
        return customer 
    
    def get_queryset(self):
        
        return super().get_queryset().filter(is_staff=False,is_admin=False)
    
class Customer(User):
    
    objects = CustomerManager()
    
    class Meta:

        proxy = True 


