from django.shortcuts import render
from django.http import HttpResponse
from .models import studentdetails
# Create your views here.


def HomeView(request):
	
	return render(request, "index.html")


def StudentsView(request):
	students = studentdetails.objects.all()
	
	return render(request,"students.html",{'students': students})