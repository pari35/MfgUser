from django.http import JsonResponse
from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

from .models import AddUser
# from .forms import AddUsers

#add user 
def add_user(request):
    if request.method == 'POST':

        # form = AddUsers(request.POST)
        # print(form)
        # if form.is_valid():
        #     form.save()
        form = AddUser(
            first_name = request.POST.get("firstname"),
            last_name = request.POST.get("lastname"),
            email = request.POST.get("username"),
            role = request.POST.get("userrole")
        ).save()
        
        messages.success(request, "user added")
        # return redirect(request, "add.html")
        return redirect("add_user") 

        # return render("add.html")
        # return render(request,'add.html')
        
        print(form.errors)
            
            
    else:
        form = AddUser()
    context = {
        
    }

    aduser=AddUser.objects.all
    return render(request,'add_new_user.html',{'aduser':aduser})
    

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
    """
    old_user = None
    try:
        # old_user = AddUser.objects.get(id=id)
        old_user = AddUser.objects.get(id=request.POST.get("id"))
    except:
        pass
    if old_user:
    # if request.method == 'POST':
        form = AddUsers(request.POST,request.FILES,instance=AddUser)
        if form.is_valid():
            form.save()
            return redirect('designation_list')
        else:
            print(form.errors)
    # else:
        form = AddUser(instance=AddUser)
        
    else:
       
        return redirect('update_user')

    return render(request, 'edit_user.html', )
    """
    user_update = None
    if request.method == "POST":
        user_update = AddUser.objects.get(id = request.POST.get("id"))
        return render(request, "edit_user.html", {"user" : user_update})
    return render(request, "edit_user.html", {"user" : user_update})

def update_user_DB(request):
    if request.method == "POST":
        
        usr = AddUser.objects.get(id = request.POST.get("idd"))
        
       
        usr.first_name = request.POST.get("firstname")
       
        usr.last_name=request.POST.get("lastname")
        usr.username=request.POST.get("username")
        usr.userrole=request.POST.get("userrole")
        usr.email=request.POST.get("email")
        usr.save()
        return render(request,'user_mgmt.html',{"aduser" : AddUser.objects.all()})
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

def login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.isAuthenticated:
                pass
        return render(request,'user_mgmt.html', {"aduser" : AddUser.objects.all()})
        print('user logged in')
        
    return render(request,'login.html')