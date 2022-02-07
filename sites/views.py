from urllib import response
from django.shortcuts import render, render_to_response

# Create your views here.
def sites(request):
    return render(request,'sites.html')