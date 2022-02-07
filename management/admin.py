from sqlite3 import connect
from django.contrib import admin
from .models import *


@admin.register(AddUser)
class AddUser(admin.ModelAdmin):
    list_display=('first_name','last_name','email','role','profile_pic')


@admin.register(Status)
class Status(admin.ModelAdmin):
    status =('status')


@admin.register(SiteDetails)
class SiteDetail(admin.ModelAdmin):
    
    sites=('station_id','station_name','add_line1','add_line2')


@admin.register(AddConnector)
class connector(admin.ModelAdmin):
    
    connect=('connector_type','connector_id','connector_name','status','plug_type_name','max_charge_rate','tariff_amount','tariff_currency')

@admin.register(ChargePoint)
class ChargePt(admin.ModelAdmin):
    chargept =('charge_id','charge_name','status','back_office','device_id')
