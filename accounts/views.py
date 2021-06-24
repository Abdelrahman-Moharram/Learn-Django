from django.shortcuts import redirect, render
from .forms import addUserTips
from .models import userTips
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
def login_user(request):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                        login(request, user)
                        try:
                                tipsData = userTips.objects.get(user_id=user.id)
                                request.session['image'] = str(tipsData.userImage)
                                request.session['userType'] = tipsData.userType
                        except:
                            pass
                        
                                
                        request.session['id'] = user.id
                        request.session['first_name'] = user.first_name
                        request.session['last_name'] = user.last_name
                        request.session['email'] = user.email
                        request.session['username'] = user.username
                        request.session['is_superuser'] = user.is_superuser
                        request.session['date'] = str(user.date_joined)

                        
                        
                        if user.is_superuser:
                                return redirect("/admin")
                        else:
                                return redirect("home:index")
                else:
                        pass
        return render(request,'accounts/login.html', {})

def register(request):
        if request.method == "POST":
                if request.POST['password'] == request.POST['confirm_password']:
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
                                login(request, user)
                                try:
                                        tipsData = userTips.objects.get(user_id=user.id)
                                        request.session['image'] = str(tipsData.userImage)
                                        request.session['userType'] = tipsData.userType
                                except:
                                    pass
                                request.session['id'] = user.id
                                request.session['first_name'] = user.first_name
                                request.session['last_name'] = user.last_name
                                request.session['email'] = user.email
                                request.session['username'] = user.username
                                request.session['is_superuser'] = user.is_superuser
                                
                                return redirect("home:index")
                        else:
                                return redirect("jobs:jobLis")
                
        return render(request,'accounts/register.html', {'addUserTips':addUserTips()})

def logout_user(request):
        logout(request)
        return redirect("home:index")
