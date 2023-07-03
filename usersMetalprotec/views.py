from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginSystem(request):
    if request.method == 'POST':
        userUsername = request.POST.get('userUsername')
        userPassword = request.POST.get('userPassword')
        userSystem = authenticate(request,username=userUsername,password=userPassword)
        if userSystem is not None:
            login(request,userSystem)
            return HttpResponseRedirect(reverse('usersMetalprotec:welcomeMetalprotec'))
        else:
            return HttpResponseRedirect(reverse('usersMetalprotec:loginSystem'))
    return render(request,'loginSystem.html')

@login_required(login_url='/')
def welcomeMetalprotec(request):
    return render(request,'welcomeMetalprotec.html')

@login_required(login_url='/')
def usersMetalprotec(request):
    return render(request,'usersMetalprotec.html')

@login_required(login_url='/')
def logoutSystem(request):
    logout(request)
    return HttpResponseRedirect(reverse('usersMetalprotec:loginSystem'))