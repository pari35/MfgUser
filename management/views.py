from django.shortcuts import render ,redirect
from django.contrib import messages

from .models import AddUser, ProfilePic
from .forms import AddUsers

#add user 
def add_user(request):
    if request.method == 'POST':
        # form = AddUser(request.form)
        form = AddUser(
            first_name = request.POST.get("firstname"),
            last_name = request.POST.get("lastname"),
            email = request.POST.get("username"),
            role = request.POST.get("userrole")
        )
        form.save()
        
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
    return render(request, "search_results.html", {"results" : search_results})


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

    

