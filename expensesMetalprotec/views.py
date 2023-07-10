from django.shortcuts import render
from .models import departmentCost, categoryCost, divisionCost,costRegister, boxRegister, cashIncome
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import datetime

# Create your views here.

def boxRegisterFunction(request):
    if request.method == 'POST':
        currencyBox = request.POST.get('currencyBox')
        descriptionBox = request.POST.get('descriptionBox')
        valueBox = request.POST.get('valueBox')
        creationDate = datetime.datetime.today()
        boxRegister.objects.create(
            descriptionBox=descriptionBox,
            valueBox=valueBox,
            creationDate=creationDate,
            currencyBox=currencyBox,
            endpointBox=request.user.extendeduser.endpointUser,
        )
        return HttpResponseRedirect(reverse('expensesMetalprotec:boxRegisterFunction'))
    return render(request,'boxRegister.html',{
        'boxRegisterSystem':boxRegister.objects.filter(endpointBox=request.user.extendeduser.endpointUser).order_by('id')
    })

def costRegisterFunction(request):
    tc_compra = 3.62
    if request.method == 'POST':
        if 'nuevoCosto' in request.POST:
            identificationCost = request.POST.get('identificationCost')
            dateRegistered=request.POST.get('dateRegistered')
            dateRegistered = datetime.datetime.strptime(dateRegistered,'%Y-%m-%d')
            rucCost=request.POST.get('rucCost')
            descriptionCost=request.POST.get('descriptionCost')
            valueCost=request.POST.get('valueCost')
            currencyCost=request.POST.get('currencyCost')
            divisionInfo=request.POST.get('divisionInfo')
            objDivision = divisionCost.objects.get(id=divisionInfo)
            costRegister.objects.create(
                asociatedDivision=objDivision,
                dateRegistered=dateRegistered,
                identificationCost=identificationCost,
                rucCost=rucCost,
                descriptionCost=descriptionCost,
                quantityCost=valueCost,
                currencyCost=currencyCost,
                endpointCost=request.user.extendeduser.endpointUser,
            )
            return HttpResponseRedirect(reverse('expensesMetalprotec:costRegisterFunction'))
        elif 'asignar' in request.POST:
            idBoxInfo = request.POST.get('idBoxInfo')
            registerxBoxInfo = request.POST.get('registerxBoxInfo')
            registerUpdate = costRegister.objects.get(id=registerxBoxInfo)
            passBox = registerUpdate.asociatedBox
            if passBox is not None:
                if passBox.currencyBox == 'SOLES':
                    if registerUpdate.currencyCost == 'SOLES':
                        passBox.valueBox = str(round(float(passBox.valueBox) + float(registerUpdate.quantityCost),2))
                        passBox.save()
                    if registerUpdate.currencyCost == 'DOLARES':
                        passBox.valueBox = str(round(float(passBox.valueBox) + float(registerUpdate.quantityCost)*tc_compra,2))
                        passBox.save()
                if passBox.currencyBox == 'DOLARES':
                    if registerUpdate.currencyCost == 'SOLES':
                        passBox.valueBox = str(round(float(passBox.valueBox) + float(registerUpdate.quantityCost)/tc_compra,2))
                        passBox.save()
                    if registerUpdate.currencyCost == 'DOLARES':
                        passBox.valueBox = str(round(float(passBox.valueBox) + float(registerUpdate.quantityCost),2))
                        passBox.save()
            if idBoxInfo != '':
                relatedBox = boxRegister.objects.get(id=idBoxInfo)
                registerUpdate.asociatedBox = relatedBox
                registerUpdate.save()
                if relatedBox.currencyBox == 'SOLES':
                    if registerUpdate.currencyCost == 'SOLES':
                        relatedBox.valueBox = str(round(float(relatedBox.valueBox) - float(registerUpdate.quantityCost),2))
                        relatedBox.save()
                    if registerUpdate.currencyCost == 'DOLARES':
                        relatedBox.valueBox = str(round(float(relatedBox.valueBox) - float(registerUpdate.quantityCost)*tc_compra,2))
                        relatedBox.save()
                if relatedBox.currencyBox == 'DOLARES':
                    if registerUpdate.currencyCost == 'SOLES':
                        relatedBox.valueBox = str(round(float(relatedBox.valueBox) - float(registerUpdate.quantityCost)/tc_compra,2))
                        relatedBox.save()
                    if registerUpdate.currencyCost == 'DOLARES':
                        relatedBox.valueBox = str(round(float(relatedBox.valueBox) - float(registerUpdate.quantityCost),2))
                        relatedBox.save()
                return HttpResponseRedirect(reverse('expensesMetalprotec:costRegisterFunction'))
            else:
                registerUpdate.asociatedBox = None
                registerUpdate.save()
                return HttpResponseRedirect(reverse('expensesMetalprotec:costRegisterFunction'))
    return render(request,'costRegister.html',{
        'divisionsSystem':divisionCost.objects.filter(endpointDivision=request.user.extendeduser.endpointUser),
        'costRegistersSystem':costRegister.objects.filter(endpointCost=request.user.extendeduser.endpointUser),
        'boxRegistersSystem':boxRegister.objects.filter(endpointBox=request.user.extendeduser.endpointUser),
    })

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
    
def getDivisionData(request):
    idDivision = request.GET.get('idDivision')
    objDivision = divisionCost.objects.get(id=idDivision)
    categoryInfo = objDivision.asociatedCategory.nameCategory
    deparmentInfo = objDivision.asociatedCategory.asociatedDeparment.nameDeparment
    typeCost = objDivision.typeCost
    behavior = objDivision.behavior
    operativeCost = objDivision.operativeCost
    print(operativeCost)
    return JsonResponse({
        'categoryInfo':categoryInfo,
        'deparmentInfo':deparmentInfo,
        'typeCost':typeCost,
        'behavior':behavior,
        'operativeCost':operativeCost
    })

def deleteCostRegister(request,idRegister):
    registerCostData = costRegister.objects.get(id=idRegister)
    registerCostData.delete()
    return HttpResponseRedirect(reverse('expensesMetalprotec:costRegisterFunction'))

def getDataRegisterInfo(request):
    idRegisterInfo = request.GET.get('idRegisterInfo')
    objRegister = costRegister.objects.get(id=idRegisterInfo)
    return JsonResponse({
        'razonCosto':objRegister.identificationCost,
        'fechaCosto':objRegister.dateRegistered.strftime("%d-%m-%Y"),
        'rucCosto':objRegister.rucCost,
        'conceptoCosto': objRegister.descriptionCost,
        'importeCosto': objRegister.quantityCost,
        'monedaCosto': objRegister.currencyCost,
        'divisionCosto': objRegister.asociatedDivision.nameDivision,
        'categoriaCosto': objRegister.asociatedDivision.asociatedCategory.nameCategory,
        'departamentoCosto': objRegister.asociatedDivision.asociatedCategory.asociatedDeparment.nameDeparment,
        'tipoCosto': objRegister.asociatedDivision.typeCost,
        'comportamientoCosto': objRegister.asociatedDivision.behavior,
        'operativoCosto': objRegister.asociatedDivision.operativeCost,
    })

def deleteBoxRegister(request,idBoxRegister):
    boxRegisterInfo = boxRegister.objects.get(id=idBoxRegister)
    boxRegisterInfo.delete()
    return HttpResponseRedirect(reverse('expensesMetalprotec:boxRegisterFunction'))

def showBoxInfo(request,idBoxRegister):
    asociatedBox = boxRegister.objects.get(id=idBoxRegister)
    registersBoxInfo = costRegister.objects.filter(endpointCost=request.user.extendeduser.endpointUser).filter(asociatedBox=asociatedBox)
    cashIncomeBoxInfo = cashIncome.objects.filter(endpointIncome=request.user.extendeduser.endpointUser).filter(asociatedBox=asociatedBox)
    return render(request,'boxDetailInfo.html',{
        'asociatedBox':asociatedBox,
        'registersBoxInfo':registersBoxInfo,
        'cashIncomeBoxInfo':cashIncomeBoxInfo,
    })

def createIncomeBox(request,idBoxInfo):
    if request.method == 'POST':
        quantityIncome=request.POST.get('quantityIncome')
        dateRegistered=request.POST.get('dateRegistered')
        dateRegistered = datetime.datetime.strptime(dateRegistered,'%Y-%m-%d')
        descriptionIncome = request.POST.get('descriptionIncome')
        boxUpdateInfo = boxRegister.objects.get(id=idBoxInfo)
        boxUpdateInfo.valueBox = str(round(float(boxUpdateInfo.valueBox) + float(quantityIncome),2))
        boxUpdateInfo.save()
        cashIncome.objects.create(
            asociatedBox=boxUpdateInfo,
            dateRegistered=dateRegistered,
            descriptionIncome=descriptionIncome,
            quantityIncome=quantityIncome,
            endpointIncome=request.user.extendeduser.endpointUser,
        )
        return HttpResponseRedirect(reverse('expensesMetalprotec:showBoxInfo', kwargs={'idBoxRegister':idBoxInfo}))
    
def deleteCashIncome(request,idCashIncome, idBoxRegister):
    cashIncomeDelete = cashIncome.objects.get(id=idCashIncome)
    passBox = cashIncomeDelete.asociatedBox
    passBox.valueBox = str(round(float(passBox.valueBox) - float(cashIncomeDelete.quantityIncome),2))
    passBox.save()
    cashIncomeDelete.delete()
    return HttpResponseRedirect(reverse('expensesMetalprotec:showBoxInfo', kwargs={'idBoxRegister':idBoxRegister}))