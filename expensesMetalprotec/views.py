from django.shortcuts import render
from .models import departmentCost, categoryCost, divisionCost
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

# Create your views here.

def boxRegister(request):
    return render(request,'boxRegister.html')

def costRegister(request):
    return render(request,'costRegister.html')

def datacenter(request):
    return render(request,'datacenter.html',{
        'divisionsSystem':divisionCost.objects.filter(endpointDivision=request.user.extendeduser.endpointUser).order_by('id'),
        'deparmentsSystem':departmentCost.objects.filter(endpointDeparment=request.user.extendeduser.endpointUser).order_by('id'),
        'categoriesSystem':categoryCost.objects.filter(endpointCategory=request.user.extendeduser.endpointUser).order_by('id'),
    })

def purchaseOrder(request):
    return render(request,'purchaseOrder.html')

def deleteDivision(request,idDivision):
    divisionCost.objects.get(id=idDivision).delete()
    return HttpResponseRedirect(reverse('expensesMetalprotec:datacenter'))

def deleteCategory(request,idCategory):
    categoryCost.objects.get(id=idCategory).delete()
    return HttpResponseRedirect(reverse('expensesMetalprotec:datacenter'))
    
def deleteDeparment(request,idDeparment):
    departmentCost.objects.get(id=idDeparment).delete()
    return HttpResponseRedirect(reverse('expensesMetalprotec:datacenter'))

def newDeparment(request):
    if request.method == 'POST':
        nameDeparment = request.POST.get('nameDeparment')
        departmentCost.objects.create(
            nameDeparment=nameDeparment,
            endpointDeparment=request.user.extendeduser.endpointUser,
        )
        return HttpResponseRedirect(reverse('expensesMetalprotec:datacenter'))
    
def newCategory(request):
    if request.method == 'POST':
        nameCategory = request.POST.get('nameCategory')
        idDeparment = request.POST.get('idDeparment')
        deparmentSystem = departmentCost.objects.get(id=idDeparment)
        categoryCost.objects.create(
            asociatedDeparment=deparmentSystem,
            nameCategory=nameCategory,
            endpointCategory=request.user.extendeduser.endpointUser,
        )
        return HttpResponseRedirect(reverse('expensesMetalprotec:datacenter'))
    
def getCategories(request):
    categoriesxDeparment = []
    idDeparment = request.GET.get('idDeparment')
    selectedDeparment = departmentCost.objects.get(id=idDeparment)
    categoriesSystem = categoryCost.objects.filter(endpointCategory=request.user.extendeduser.endpointUser).filter(asociatedDeparment=selectedDeparment)
    for categorieInfo in categoriesSystem:
        categoriesxDeparment.append([str(categorieInfo.id),str(categorieInfo.nameCategory)])
    return JsonResponse({
        'categoriesxDeparment':categoriesxDeparment,
    })

def newDivision(request):
    if request.method == 'POST':
        idCategory = request.POST.get('idCategory')
        typeCost = request.POST.get('typeCost')
        behavior = request.POST.get('behavior')
        nameDivision = request.POST.get('nameDivision')
        operativeCost = request.POST.get('operativeCost')
        asociatedCategory = categoryCost.objects.get(id=idCategory)
        divisionCost.objects.create(
            asociatedCategory=asociatedCategory,
            nameDivision=nameDivision,
            typeCost=typeCost,
            behavior=behavior,
            operativeCost=operativeCost,
            endpointDivision=request.user.extendeduser.endpointUser,
        )
        return HttpResponseRedirect(reverse('expensesMetalprotec:datacenter'))