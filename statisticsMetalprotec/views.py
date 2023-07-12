from django.shortcuts import render

# Create your views here.
def mainDashboard(request):
    return render(request,'mainDashboard.html')

def clientsDashboard(request):
    return render(request,'clientsDashboard.html')

def productsDashboard(request):
    return render(request,'productsDashboard.html')

def sellDashboard(request):
    return render(request,'sellDashboard.html')