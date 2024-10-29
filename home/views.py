from django.shortcuts import render

from django.http import HttpResponse

from .models import Resource

from .models import Packages
from  .filters import PackagesFilter


# Create your views here.
def home(request):
    
    return render(request,'home.html') 

def about(request):
    return render(request,'about.html') 

def resources(request):
    
    QueryAllData=Resource.objects.all()
    
    context={'resources':QueryAllData}
    
    return render(request,'resources.html',context=context) 

def packages(request):
    packages_list=Packages.objects.all()
    package_filter=PackagesFilter(request.GET,queryset=packages_list)
    return render(request,'packages.html',{'filter':package_filter})
    
       
def my_login(request):
    return render(request,'my-login.html') 

def register(request):
    return render(request,'register.html') 


