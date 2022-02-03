from django.contrib import admin
from .models import AddUser,ProfilePic


@admin.register(AddUser)
class AddUser(admin.ModelAdmin):
    list_display=('first_name','last_name','email','role')


# @admin.register(ProfilePic)
# class ProflePic(admin.ModelAdmin):
#     list_display =('profile_pic')
# Register your models here.

