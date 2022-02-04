from django.contrib import admin
from .models import AddUser , Status


@admin.register(AddUser)
class AddUser(admin.ModelAdmin):
    list_display=('first_name','last_name','email','role','profile_pic')


@admin.register(Status)
class Status(admin.ModelAdmin):
    status =('status')

