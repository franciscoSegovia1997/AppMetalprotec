from django.shortcuts import render
from . models import bankSystem
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def bankRegisters(request):
    if request.method == 'POST':
        nameBank = request.POST.get('nameBank')
        currencyBank = request.POST.get('currencyBank')
        accountNumber = request.POST.get('accountNumber')
        moneyBank = request.POST.get('moneyBank')
        bankSystem.objects.create(
            nameBank=nameBank,
            currencyBank=currencyBank,
            accountNumber=accountNumber,
            moneyBank=moneyBank,
            endpointBank=request.user.extendeduser.endpointUser,
        )
    return render(request,'bankRegisters.html',{
        'bankRegistersSystem':bankSystem.objects.filter(endpointBank=request.user.extendeduser.endpointUser)
    })

def comissions(request):
    return render(request,'comissions.html')

def paymentsRegister(request):
    return render(request,'paymentsRegister.html')

def deleteBankRegister(request,idBank):
    bankSystem.objects.get(id=idBank).delete()
    return HttpResponseRedirect(reverse('financeMetalprotec:bankRegisters'))