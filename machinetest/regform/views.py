from django.shortcuts import render
from .models import *

# Create your views here.

def home (request):
    all=form.objects.all()
    context={
        "all":all,
    }
    return render(request,'form.html')


def forms(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        
        
        forms=form.objects.create(name=name,mailid=email,password=password,phonenumber=phonenumber)
        forms.save()
        return render(request,'success.html')