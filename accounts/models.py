from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(unique=True,max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    date_joined = models.DateField(auto_now_add=True)
    

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
