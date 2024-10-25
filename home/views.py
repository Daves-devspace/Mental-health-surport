from django.shortcuts import render

from django.http import HttpResponse

from .models import Resource

# Create your views here.
def home(request):
    
    return render(request,'home.html') 
def resources(request):
    
    QueryAllData=Resource.objects.all()
    
    context={'resources':QueryAllData}
    
    return render(request,'resources.html',context=context) 
       
def my_login(request):
    return render(request,'my-login.html') 

def register(request):
    return render(request,'register.html') 


