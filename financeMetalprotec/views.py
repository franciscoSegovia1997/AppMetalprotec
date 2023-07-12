from django.shortcuts import render

# Create your views here.
def bankRegisters(request):
    return render(request,'bankRegisters.html')

def comissions(request):
    return render(request,'comissions.html')

def paymentsRegister(request):
    return render(request,'paymentsRegister.html')