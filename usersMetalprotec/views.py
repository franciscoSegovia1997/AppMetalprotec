from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginSystem(request):
    return render(request,'loginSystem.html')

def usersMetalprotec(request):
    return render(request,'users.html')