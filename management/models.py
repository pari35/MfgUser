from django.db import models

from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.

class AddUser(models.Model):
    """user details"""
    first_name        = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20,)
    email          =models.CharField(max_length=20)
    role           = models.CharField(max_length=20)

 
# class UserAuth(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

class ProfilePic(models.Model):
    profile_pic = models.ImageField(upload_to="static/images",default="")