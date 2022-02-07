from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from .forms import AddUsers, AddSite
import csv

from .models import AddUser




#add user 
def add_user(request):
    form = AddUsers()
    if request.method == 'POST':

        form = AddUsers(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            print("form saved successfully")

    if request.method =="POST":
       
        username=request.POST['username']
        password=request.POST['password']

        # if User.objects.filter(username=username).exists():
        #     print('username taken')
        user=User.objects.create_user(username=username,password=password)
        user.save()
        print('user created')
    adeduser=User.objects.all()   
    aduser=AddUser.objects.all()
    return render(request,'add_new_user.html',{'aduser':aduser,"form" : form,'adeduser':adeduser})
    

def user_management(request):
    aduser=AddUser.objects.all
    return render(request,'user_mgmt.html',{'aduser':aduser})

def search(request):
    query = None
    if request.method == "GET":
        query = request.GET["query"]

    name_in_query = AddUser.objects.filter(first_name__icontains=query)
    email_in_query = AddUser.objects.filter(first_name__icontains=query)

    search_results = (name_in_query | email_in_query).distinct()
    # print("search results : ", search_results)
    return render(request, "user_mgmt.html", {"aduser" : search_results})


def update_user(request):
    form = AddUsers()

    old_user = None
    if request.method == "POST":
        try:
            # old_user = AddUser.objects.get(id=id)
            old_user = AddUser.objects.get(id=request.POST.get("id"))
            
        except:
            pass
        if old_user:
            # if request.method == 'POST':
            form = AddUsers(request.POST,request.FILES,instance=old_user)
            # form = AddUsers(request.POST,request.FILES)
            # if form.is_valid():

            form.save()
            print("form updated")
            return redirect('user_mgmt')
        # else:
        #     print(form.errors)
        # else:
        # form = AddUser(instance=AddUser)
        # form = AddUser()
            
        else:
        
            return redirect('update_user', )
        form = AddUser()

    return render(request, 'edit_user.html', )

    

def update_user_DB(request):
    if request.method == "POST":
        
        usr = AddUser.objects.get(id = request.POST.get("idd"))
        
       
        usr.first_name = request.POST.get("firstname")
       
        usr.last_name=request.POST.get("lastname")
        usr.username=request.POST.get("username")
        usr.userrole=request.POST.get("userrole")
        usr.email=request.POST.get("email")
        usr.save()
    # return render(request,'user_mgmt.html',{"aduser" : AddUser.objects.all()})
        # return JsonResponse({"status" : "success"})
    # return render(request, "")

def user_register(request):
    if request.method =="POST":
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        # if User.objects.filter(username=username).exists():
        #     print('username taken')
        user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
        user.save()
        print('user created')
    return render(request,'register.html')

def admin_user_create(request):
    if request.method =="POST":
       
        username=request.POST['username']
        password=request.POST['password']

        # if User.objects.filter(username=username).exists():
        #     print('username taken')
        user=User.objects.create_user(username=username,password=password)
        user.save()
        print('user created')
    # return render(request,'add_new_user.html')

def loginn(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print (username, password)
        # user=auth.authenticate(username=username,password=password)
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            # login()
            return redirect("user_management")
        return render(request,'user_mgmt.html', {"aduser" : AddUser.objects.all()})
        print('user logged in')
        
    return render(request,'login.html')

def sites(request):
    form=AddSite
    if request.method == 'POST':
        form = AddSite(request.POST,)
        
        if form.is_valid():
            form.save()
            messages.success(request,'Site details added')
            print('added')
        else:
            print(form.errors)
            
            
    return render(request,'sites.html',{'form':form})