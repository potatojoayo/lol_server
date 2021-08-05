from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework.authtoken.models import Token
from product.models import Product

    
class UserManager(BaseUserManager):

    def create_user(self,email,name,password=None):
        user = self.model(
            email = self.normalize_email(email),
            name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):

    objects = UserManager()
    #필수사항
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    # option
    email = models.CharField(max_length=50,unique=True)
    name  = models.CharField(max_length=50)
    phone = models.CharField(max_length=15,null=True,blank=True)
    pcc = models.CharField(max_length=13,null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=20,null=True,blank=True)
    bank_account = models.CharField(max_length=50,null=True,blank=True)
    last_login = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(Product,related_name='liked_by',blank=True)
    carts = models.ManyToManyField(Product,related_name='carted_by',through='Cart',blank=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

