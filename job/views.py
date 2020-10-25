from django.shortcuts import render,HttpResponse
from .models import job
from django.core.paginator import Paginator
from .forms import applyform,add
from django.contrib import messages
# Create your views here.

def jobs (request):

    pag   = Paginator(job.objects.all(),10)

    return render(request,'job/jobs.html',{"jobs":pag.get_page(request.GET.get('page'))})


def job_details( request, slug):
    jobs = job.objects.get(slug=slug)

    if request.method == 'POST':
        form = applyform(request.POST ,request.FILES)
        if form.is_valid():
            
            form = form.save(commit=False)
            form.job = jobs
            form.save()
            messages.success(request,'Applied Successfully')

    
    return render(request,'job/job_details.html',{"details":jobs})



def addJob(request):

    if request.method == "POST":
        form = add(request.POST , request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            messages.success(request,"Posted Successfully")
    form = add()
    return render(request,'job/add.html',{"form":form})