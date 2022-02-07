from pyexpat import model
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
    profile_pic = models.ImageField(upload_to="static/images",default="",null=True,blank=True)
 
class Status(models.Model):
    status=models.CharField(max_length=10)
                 

class SiteDetails(models.Model):
    station_id=  models.CharField(max_length=20)
    station_name=   models.CharField(max_length=20)
    add_line1 = models.CharField(max_length=50)
    add_line2 =models.CharField(max_length=30)
    add_line3 = models.CharField(max_length=30)

class AddConnector(models.Model):
    connector_type= models.CharField(max_length=20)
    connector_id =models.CharField(max_length=20)
    connector_name =models.CharField(max_length=20)
    status =        models.CharField(max_length=20)
    plug_type_name = models.CharField(max_length=20)
    max_charge_rate = models.CharField(max_length=20)
    tariff_amount   =models.CharField(max_length=20)
    tariff_currency =models.CharField(max_length=20)

class ChargePoint(models.Model):
    charge_id = models.CharField(max_length=20)
    charge_name = models.CharField(max_length=20)
    status =  models.CharField(max_length=20)
    back_office =  models.CharField(max_length=20)
    device_id =   models.IntegerField()