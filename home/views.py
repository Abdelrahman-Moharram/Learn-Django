from urllib.request import Request
from django.shortcuts import render, redirect
from .models import File

def index(request):
	if request.method == "POST":
		# print("\n\n   ==> ",str(request.FILES['file']).split("."))
		file = File.objects.create(file=request.FILES['file'], extension=str(request.FILES['file']).split(".")[1])
		file.save()
		# return redirect("home:index")
	return render(request, 'home/index.html', {'files':File.objects.all()})


def delete(request, id):
	file = File.objects.get(id=id)
	file.delete()
	return redirect("home:index")