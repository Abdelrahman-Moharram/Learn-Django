from django.shortcuts import render,redirect
from .models import Job,Category
from django.core.paginator import Paginator
from .form import emp_application
def jobList(request):
	

	paginator = Paginator(Job.objects.all(),1)
 
	pNum = request.GET.get("page")
	
	pObjs = paginator.get_page(pNum)

 
	return render(request,'job/allJobs.html', {'jobs':pObjs})
	

def jobDetail(request,slug):
        job = Job.objects.get(slug = slug)
        if request.method == 'POST':
                form = emp_application(request.POST ,request.FILES)
                if form.is_valid():
                        form = form.save(commit=False)
                        form.jobId = job
                        form.save()
                        return redirect("http://127.0.0.1:8000/jobs/")
                
        return render(request, 'job/jobDetail.html', {'job':job})
	
