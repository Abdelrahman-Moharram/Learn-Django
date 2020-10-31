from django.shortcuts import render,redirect
from .models import account,employeer,employee
from .forms import userForm,employeeForm,employeerForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

def user_register(request):
    if request.user.is_authenticated:
        messages.info(request,"YOU ALREADY SIGNED IN")
        return redirect("jobs:home")

    










    
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            

            form.save()
            messages.info(request,request.POST.get('email')+' created one step to complete')                

            return redirect("accounts:login")
            
    return render(request,'accounts/register.html',{"form":userForm()})


def create_employer(request):


    if request.method == "POST":
        form = employeerForm(request.POST ,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            data = account.objects.get(email=request.session.get('email'))

            print("\n\n\n\n\n\nemployer data>>>>>>>>>>>>>>>>>>>>>>>>>> ",data.user,"\n\n\n\n\n\n\n")
            form.user = data
            form.save()
            data = employeer.objects.get(user=data)
            
            
            
            request.session['linkedin']  = data.linkedin
            
            messages.info(request,"employer added succesfully")

            return redirect("jobs:home")
            

    return render(request,'accounts/register.html',{"form":employeerForm()})



def create_employee(request):



    if request.method == "POST":
        form = employeeForm(request.POST ,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            data = account.objects.get(email=request.session.get('email'))

            

            form.user = data
            form.save()
            data = employee.objects.get(user=data)
            print("\n\n\n\n\n\ndata>>>>>>>>>>>>>>>>>>>>>>>>>> ",data.user,"\n\n\n\n\n\n\n")
            
            
            
            request.session['linkedin']      = data.linkedin
            request.session['start_salary']  = data.start_salary
            #request.session['categery']      = data.categery
            request.session['exp']           = data.exp
            request.session['github']        = data.github
            
            messages.info(request,"employee added succesfully")

            return redirect("jobs:home")
            

    return render(request,'accounts/register.html',{"form":employeeForm()})





def user_login(request):


    if request.method == "POST":
        user = authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))

        if user is not None:
                login(request,user)
                user = account.objects.get(email=request.POST.get("email"))
                request.session["id"]            =   user.pk
                request.session['fname']         =   user.fname
                request.session['lname']         =   user.lname
                request.session['email']         =   user.email
                request.session['is_admin']      =   user.is_admin
                request.session['phone']         =   user.phone
                request.session['user_type']     =   user.user_type
                request.session['slug']          =   user.slug
                request.session['is_staff']      =   user.is_staff
                request.session['is_superuser']  =   user.is_superuser
            

        if request.session.get("is_admin") == True:
            
            redirect("127.0.0.1:8000/admin/")

        
        if request.session.get("user_type") == "employee":
            emp = employee.objects.filter(user=request.session.get("id"))
        
        elif request.session.get("user_type") == "employeer":
            emp = employeer.objects.filter(user=request.session.get("id"))
        
        print("\n\n\n\n\n\n\n\n\n125------>",emp,len(emp),"\n\n\n\n\n\n\n")


            
        if len(emp) > 0:
            return redirect("jobs:home")
            
        else:
            print("\n\n\n\n\n\n\n\n\n\n>>>>>>employee: ",employee,"employeer: ",employeer,"\n\n\n\n")
            messages.info(request,"remain one step to finish")
            if request.session.get('user_type') == "employee":
                return redirect("accounts:employee")

            elif request.session.get('user_type')  == "employeer":                

                return redirect("accounts:employer")

    
    else:
        messages.info(request,"Can't signin")                




    
    return render(request,'accounts/login.html',{})



def user_logout(request):
    logout(request)
    return redirect("jobs:home")

def profile(request, slug):
    

    return render(request,'accounts/profile.html',{})

