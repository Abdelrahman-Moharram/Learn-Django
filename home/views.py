from django.shortcuts import render
from job.models import Job,job_application
from accounts.models import userTips

def home(request):
        jobs = Job.objects.all()
        jobs = jobs[:10]
        return render(request,'home/index.html', {'jobs':jobs})

def user_profile(request,username):
        if request.session['id'] is not None:
                usertipsData = userTips.objects.get(user_id=request.session['id'])
                jobs = Job.objects.filter(employer_id=request.session['id'])
                apps = job_application.objects.filter(employee_id=request.session['id'])
        else:
                return  redirect("home:index")

        return render(request,"home/profile.html",{'userTips':usertipsData,'jobs':jobs,'apps':apps})