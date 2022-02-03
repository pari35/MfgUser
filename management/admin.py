from django.contrib import admin
from .models import AddUser


@admin.register(AddUser)
class AddUser(admin.ModelAdmin):
    list_display=('first_name','last_name','email','role','profile_pic')


# @admin.register(ProfilePic)
# class ProflePic(admin.ModelAdmin):
#     profile_pic =('profile_pic')

