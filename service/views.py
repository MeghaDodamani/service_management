import re

from django.shortcuts import render,redirect
from .forms import  RegistrationForm
from django.contrib.auth import authenticate,login


# Create your views here.
def register(request):
    if  request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Form errors:", form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        email =request.POST.get('email')
        password =request.POST.get('paassword')
        user = authenticate(request,username =email,password = password)
        if user is not None:
            login(request.user)
            return redirect('dashboard')
      
        return render(request,'accounts/login.html',{'error':'Invalid email or password'})
    return render(request,'accounts/login.html')