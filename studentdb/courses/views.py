from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses
# Create your views here.\

def CourseView(request):
	courses = Courses.objects.all()
	
	return render(request,"Courses.html",{'students': courses})