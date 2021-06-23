from django.shortcuts import redirect, render
from .forms import addUserTips
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
def login(request):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                        if user.is_superuser:
                                return redirect("/admin")
                        else:
                                return redirect("home:index")
                else:
                        pass
        return render(request,'accounts/login.html', {})

def register(request):
        if request.method == "POST":
                user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.save()
                usertips = addUserTips(request.POST)
                usertips = usertips.save(commit = False)
                usertips.user = user
                usertips.save()
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                        return redirect("home:index")
                else:
                        return redirect("jobs:jobLis")
                
        return render(request,'accounts/register.html', {'addUserTips':addUserTips()})

def logout_user(request):
        logout(request)
        return redirect("home:index")
