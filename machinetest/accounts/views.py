from django.shortcuts import render,redirect
from regform.models import *
from accounts.models import Account
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages,auth
from django.core.paginator import Paginator

# Create your views here.

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('name')
        print(email)
        password = request.POST.get('password')
        print(password)
        try:
            user = authenticate(username=email, password=password)
            print(user,"kjsdjdhfje")
            if user is not None and user.is_superuser:
                request.session['username'] = email
                login(request, user)
                return redirect('list')
            else:
                print("else1")
                return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
        except Account.DoesNotExist:
            print("else2")
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    return render(request, "login.html")



def listofapplication(request):
    all=form.objects.all()
    paginator=Paginator(all,5)
    page=request.GET.get('page')
    paged_form=paginator.get_page(page)
    return render(request,'list.html',{'all':paged_form})

def logoutadmin(request):
    if 'username' in request.session:
        request.session.flush()
    logout(request)
    return redirect(signin) 