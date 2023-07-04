from django.shortcuts import render
from .models import serviceSystem
from settingsMetalprotec.models import endpointSystem
from decimal import Decimal, DecimalException,getcontext
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

getcontext().prec = 10

# Create your views here.
@login_required(login_url='/')
def servicesMetalprotec(request):
    if request.method == 'POST':
        nameService = request.POST.get('nameService')
        categoryService = request.POST.get('categoryService')
        subCategoryService = request.POST.get('subCategoryService')
        measureUnit = request.POST.get('measureUnit')
        pvnIGV = str(Decimal('%.2f' % Decimal(request.POST.get('pvnIGV'))))
        pvcIGV = str(Decimal('%.2f' % (Decimal(pvnIGV)*Decimal(1.18))))
        endpointService = request.user.extendeduser.endpointUser

        serviceSystem.objects.create(
            nameService=nameService,
            categoryService=categoryService,
            subCategoryService=subCategoryService,
            measureUnit=measureUnit,
            pvnIGV=pvnIGV,
            pvcIGV=pvcIGV,
            endpointService=endpointService,
        )
        return HttpResponseRedirect(reverse('servicesMetalprotec:servicesMetalprotec'))
    return render(request,'servicesMetalprotec.html',{
        'servicesSystem':serviceSystem.objects.filter(endpointService=request.user.extendeduser.endpointUser),
    })

@login_required(login_url='/')
def deleteService(request):
    if request.method == 'POST':
        deleteIdService = request.POST.get('deleteIdService')
        deleteService = serviceSystem.objects.get(id=deleteIdService)
        deleteService.delete()
        return HttpResponseRedirect(reverse('servicesMetalprotec:servicesMetalprotec'))
    
@login_required(login_url='/')
def getServiceData(request):
    idService = request.GET.get('idService')
    editService = serviceSystem.objects.get(id=idService)
    return JsonResponse({
        'editNameService':editService.nameService,
        'editCategoryService':editService.categoryService,
        'editSubCategoryService':editService.subCategoryService,
        'editMeasureUnit':editService.measureUnit,
        'editPvnIGV':editService.pvnIGV,
    })

@login_required(login_url='/')
def updateService(request):
    if request.method == 'POST':
        editIdService=request.POST.get('editIdService')
        editNameService=request.POST.get('editNameService')
        editMeasureUnit=request.POST.get('editMeasureUnit')
        editCategoryService=request.POST.get('editCategoryService')
        editSubCategoryService=request.POST.get('editSubCategoryService')
        editPvnIGV=str(Decimal('%.2f' % Decimal(request.POST.get('editPvnIGV'))))
        editPvcIGV=str(Decimal('%.2f' % (Decimal(editPvnIGV)*Decimal(1.18))))

        editService = serviceSystem.objects.get(id=editIdService)
        editService.nameService=editNameService
        editService.categoryService=editCategoryService
        editService.measureUnit=editMeasureUnit
        editService.subCategoryService=editSubCategoryService
        editService.pvnIGV=editPvnIGV
        editService.pvcIGV=editPvcIGV
        editService.save()