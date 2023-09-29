from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def cdetails(request):
    co=course()
    d={'co':co}
    if request.method=='POST':
        cd=course(request.POST)
        if cd.is_valid():
            cname=cd.cleaned_data['cname']
            cfee=cd.cleaned_data['cfee']
            address=cd.cleaned_data['address']
        
        return HttpResponse('<h1 style="color:blue;"><center> data submitted successfully..</center></h1>')
    return render(request,'display_course.html',d)