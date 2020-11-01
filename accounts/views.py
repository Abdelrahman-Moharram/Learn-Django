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

        form     = userForm(request.POST ,request.FILES)
        form_emp = employeerForm(request.POST,request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.user_type = request.POST.get("user_type")
            form.save()
            data = account.objects.get(email=request.POST.get('email'))

            if form_emp.is_valid():
                form_emp = form_emp.save(commit=False)
                form_emp.user = data
                form_emp.save()

                messages.info(request,request.POST.get('email')+' created as employer account')                

                return redirect("accounts:login")
            else:
                messages.info(request,request.POST.get('email')+' error while creating employer account')
        else:
            messages.info(request,"Can't creat your email enter valid data")      

    return render(request,'accounts/register.html',{"form":userForm(),"form_emp":employeerForm(),"type":"employer"})



def create_employee(request):



    if request.method == "POST":

        form     = userForm(request.POST ,request.FILES)
        form_emp = employeeForm(request.POST,request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.user_type = request.POST.get("user_type")
            form.save()
            data = account.objects.get(email=request.POST.get('email'))

            if form_emp.is_valid():
                form_emp = form_emp.save(commit=False)
                form_emp.user = data
                form_emp.save()

                messages.info(request,request.POST.get('email')+' created as employer account')                

                return redirect("accounts:login")
            else:
                messages.info(request,request.POST.get('email')+' error while creating employer account')
        else:
            messages.info(request,"Can't creat your email enter valid data")      

    return render(request,'accounts/register.html',{"form":userForm(),"form_emp":employeeForm(),"type":"employee"})





def user_login(request):


    if request.method == "POST":
        user = authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))

        if user is not None:
                login(request,user)
                user = account.objects.get(email=request.POST.get("email"))
                empe = employeer.objects.filter(user=request.user)
                empr = employeer.objects.filter(user=request.user)
                
                request.session['fname']           =   user.fname
                request.session['lname']           =   user.lname
                request.session['phone']           =   user.phone
                request.session['email']           =   user.email
                request.session['slug']            =   user.slug
                request.session['is_admin']        =   user.is_admin
                request.session['is_staff']        =   user.is_staff
                request.session['is_superuser']    =   user.is_superuser
                request.session['user_type']       =   user.user_type
                if empr == None and empe != None:
                    request.session['user']           =   empe.user
                    request.session['cv']             =   empe.cv
                    request.session['start_salary']   =   empe.start_salary
                    request.session['categery']       =   empe.categery
                    request.session['exp']            =   empe.exp
                    request.session['linkedin']       =   empe.linkedin
                    request.session['github']         =   empe.github
                if empr != None and empe == None:
                    request.session['user']           =   empe.user
                    request.session['linkedin']       =   empe.linkedin

                
            

        if request.session.get("is_admin") == True:
            
            return redirect("127.0.0.1:8000/admin/")

        
        else:
            return redirect("jobs:home")



    
    return render(request,'accounts/login.html',{})



def user_logout(request):
    logout(request)
    return redirect("jobs:home")

def profile(request, slug):
    

    return render(request,'accounts/profile.html',{})

