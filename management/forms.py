from django.forms import ModelForm
from .models import AddUser,ProfilePic
from django import forms

class AddUsers(ModelForm):
   class Meta:
        model = AddUser
        fields='__all__'
        # fields = ['first_name','last_name','email','role']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'container','placeholder':'first_name'}), 
            'last_name':forms.TextInput(attrs={'class':'container','placeholder':'last_name'}), 
            'role':forms.TextInput(attrs={'class':'container','placeholder':'userrole'}), 
            'email':forms.TextInput(attrs={'class':'container','placeholder':'email'}), 
        }
        