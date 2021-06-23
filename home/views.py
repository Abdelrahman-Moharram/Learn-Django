from django.shortcuts import render
from job.models import Job


def home(request):
        jobs = Job.objects.all()
        jobs = jobs[:10]
        return render(request,'home/index.html', {'jobs':jobs})
	