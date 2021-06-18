from django.shortcuts import render
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
                        form.save(commit=False)
                        form.jobId = job.id
                        print("\n\n\n\n\n\n\n\n\n\n\n\n",job.id,"\n\n\n\n\n\n\n\n\n\n\n\n",)
                        form.save()
                        
                
        return render(request, 'job/jobDetail.html', {'job':job})
	
