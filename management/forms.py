from tkinter import Widget
from django.forms import ModelForm
from .models import AddUser,Status ,SiteDetails
from django import forms

class AddUsers(forms.ModelForm):
   class Meta:
        model = AddUser
        # fields= '__all__'
        fields = ['first_name','last_name','email','role']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'container','placeholder':'first_name'}), 
            'last_name':forms.TextInput(attrs={'class':'container','placeholder':'last_name'}), 
            'role':forms.TextInput(attrs={'class':'container','placeholder':'userrole'}), 
            'email':forms.TextInput(attrs={'class':'container','placeholder':'email'}), 
        }
        
class AddSite(forms.ModelForm):
    class Meta:
        model=SiteDetails
        fields=['station_id','station_name','add_line1','add_line2','add_line3']
        widgets={
          'station_id' :forms.TextInput(attrs={'class':'form-control my-3','placeholder':'stationID'}),  
         'station_name': forms.TextInput(attrs={'class':'form-control my-3','placeholder':'station Name'})
        }
