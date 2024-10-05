from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from .manager import UserManager
# Create your models here.

class user(AbstractBaseUser,PermissionsMixin):
    UserName=models.CharField( max_length=50,validators=[UnicodeUsernameValidator],unique=True);
    Email=models.CharField(max_length=100,unique=True);
    phone=models
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_date=models.DateField(auto_now_add=True)
    objects = UserManager()


    USERNAME_FIELD="UserName"
    REQUIRED_FIELDS=["Email"]

    class Meta:
        ordering=["-created_date"]
    

