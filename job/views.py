from django.shortcuts import render
from .models import Job,Category


def jobList(request):
	allJobs = Job.objects.all()

	return render(request,'job/allJobs.html', {'jobs':allJobs})
	

def jobDetail(request,id):
	
	return render(request, 'job/jobDetail.html', {'job':Job.objects.get(id = id)})
	
