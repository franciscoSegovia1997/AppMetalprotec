from django.shortcuts import render
from .models import endpointSystem
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from productsMetalprotec.models import storeSystem, productSystem, storexproductSystem

# Create your views here.
@login_required(login_url='/')
def settingsMetalprotec(request):
    if request.method=='POST':
        if 'newEndpoint' in request.POST:
            serieCoti=request.POST.get('serieCoti')
            nroCoti=request.POST.get('nroCoti')
            serieGuia=request.POST.get('serieGuia')
            nroGuia=request.POST.get('nroGuia')
            serieFactura=request.POST.get('serieFactura')
            nroFactura=request.POST.get('nroFactura')
            serieBoleta=request.POST.get('serieBoleta')
            nroBoleta=request.POST.get('nroBoleta')
            serieNotaFactura=request.POST.get('serieNotaFactura')
            nroNotaFactura=request.POST.get('nroNotaFactura')
            serieNotaBoleta=request.POST.get('serieNotaBoleta')
            nroNotaBoleta=request.POST.get('nroNotaBoleta')

            newEndpoint = endpointSystem.objects.create(
                serieCoti=serieCoti,
                nroCoti=nroCoti,
                serieGuia=serieGuia,
                nroGuia=nroGuia,
                serieFactura=serieFactura,
                nroFactura=nroFactura,
                serieBoleta=serieBoleta,
                nroBoleta=nroBoleta,
                serieNotaFactura=serieNotaFactura,
                nroNotaFactura=nroNotaFactura,
                serieNotaBoleta=serieNotaBoleta,
                nroNotaBoleta=nroNotaBoleta,
            )

            codeEndpoint = str(newEndpoint.id)
            while len(codeEndpoint) < 4:
                codeEndpoint = '0' + codeEndpoint
            codeEndpoint = 'END-' + codeEndpoint

            newEndpoint.codeEndpoint = codeEndpoint
            newEndpoint.save()
            return HttpResponseRedirect(reverse('settingsMetalprotec:settingsMetalprotec'))
        elif 'newStore' in request.POST:
            nameStore = request.POST.get('nameStore')
            dateCreation = datetime.date.today()
            endpointStore = request.user.extendeduser.endpointUser
            storeObject = storeSystem.objects.create(
                nameStore=nameStore,
                dateCreation=dateCreation,
                endpointStore=endpointStore,
            )
            allProductsInfo = productSystem.objects.filter(endpointProduct=request.user.extendeduser.endpointUser)
            for productInfo in allProductsInfo:
                allStoresxProduct = productInfo.storexproductsystem_set.all()
                if storeObject not in allStoresxProduct:
                    storexproductSystem.objects.create(
                        quantityProduct = '0',
                        asociatedProduct=productInfo,
                        asociatedStore=storeObject,
                    )
            return HttpResponseRedirect(reverse('settingsMetalprotec:settingsMetalprotec'))
    return render(request,'settingsMetalprotec.html',{
        'endpointsSystem':endpointSystem.objects.all().order_by('id'),
    })

@login_required(login_url='/')
def deleteEndpoint(request):
    if request.method == 'POST':
        deleteIdEndpoint = request.POST.get('deleteIdEndpoint')
        deleteEndpoint = endpointSystem.objects.get(id=deleteIdEndpoint)
        deleteEndpoint.delete()
        return HttpResponseRedirect(reverse('settingsMetalprotec:settingsMetalprotec'))

@login_required(login_url='/')
def getEndpointData(request):
    idEndpoint = request.GET.get('idEndpoint')
    editEndpoint = endpointSystem.objects.get(id=idEndpoint)
    return JsonResponse({
        'editSerieCoti':editEndpoint.serieCoti,
        'editNroCoti':editEndpoint.nroCoti,
        'editSerieGuia':editEndpoint.serieGuia,
        'editNroGuia':editEndpoint.nroGuia,
        'editSerieFactura':editEndpoint.serieFactura,
        'editNroFactura':editEndpoint.nroFactura,
        'editSerieBoleta':editEndpoint.serieBoleta,
        'editNroBoleta':editEndpoint.nroBoleta,
        'editSerieNotaFactura':editEndpoint.serieNotaFactura,
        'editNroNotaFactura':editEndpoint.nroNotaFactura,
        'editSerieNotaBoleta':editEndpoint.serieNotaBoleta,
        'editNroNotaBoleta':editEndpoint.nroNotaBoleta,
    })

def getDataOne(request):
    idEndpoint = request.GET.get('idEndpoint')
    editEndpoint = endpointSystem.objects.get(id=idEndpoint)
    return JsonResponse({
        'editSerieCoti':editEndpoint.serieCoti,
        'editNroCoti':editEndpoint.nroCoti,
        'editSerieGuia':editEndpoint.serieGuia,
        'editNroGuia':editEndpoint.nroGuia,
        'editSerieFactura':editEndpoint.serieFactura,
        'editNroFactura':editEndpoint.nroFactura,
        'editSerieBoleta':editEndpoint.serieBoleta,
        'editNroBoleta':editEndpoint.nroBoleta,
        'editSerieNotaFactura':editEndpoint.serieNotaFactura,
        'editNroNotaFactura':editEndpoint.nroNotaFactura,
        'editSerieNotaBoleta':editEndpoint.serieNotaBoleta,
        'editNroNotaBoleta':editEndpoint.nroNotaBoleta,
    })

def getDataAll(request):
    if request.method != 'GET':
        return JsonResponse({'message': 'Método no permitido'}, status=405)
    data = endpointSystem.objects.all().order_by('id')
    data_list = list(data.values())
    return JsonResponse(data_list, safe=False)

@login_required(login_url='/')
def updateEndpoint(request):
    if request.method == 'POST':
        editIdEndpoint = request.POST.get('editIdEndpoint')
        editSerieCoti=request.POST.get('editSerieCoti')
        editNroCoti=request.POST.get('editNroCoti')
        editSerieGuia=request.POST.get('editSerieGuia')
        editNroGuia=request.POST.get('editNroGuia')
        editSerieFactura=request.POST.get('editSerieFactura')
        editNroFactura=request.POST.get('editNroFactura')
        editSerieBoleta=request.POST.get('editSerieBoleta')
        editNroBoleta=request.POST.get('editNroBoleta')
        editSerieNotaFactura=request.POST.get('editSerieNotaFactura')
        editNroNotaFactura=request.POST.get('editNroNotaFactura')
        editSerieNotaBoleta=request.POST.get('editSerieNotaBoleta')
        editNroNotaBoleta=request.POST.get('editNroNotaBoleta')

        editEndpoint = endpointSystem.objects.get(id=editIdEndpoint)
        editEndpoint.serieCoti=editSerieCoti
        editEndpoint.nroCoti=editNroCoti
        editEndpoint.serieGuia=editSerieGuia
        editEndpoint.nroGuia=editNroGuia
        editEndpoint.serieFactura=editSerieFactura
        editEndpoint.nroFactura=editNroFactura
        editEndpoint.serieBoleta=editSerieBoleta
        editEndpoint.nroBoleta=editNroBoleta
        editEndpoint.serieNotaFactura=editSerieNotaFactura
        editEndpoint.nroNotaFactura=editNroNotaFactura
        editEndpoint.serieNotaBoleta=editSerieNotaBoleta
        editEndpoint.nroNotaBoleta=editNroNotaBoleta
        editEndpoint.save()
        return HttpResponseRedirect(reverse('settingsMetalprotec:settingsMetalprotec'))

@login_required(login_url='/')
def deleteStore(request):
    deleteIdStore = request.POST.get('deleteIdStore')
    deleteStore = storeSystem.objects.get(id=deleteIdStore)
    deleteStore.delete()
    return HttpResponseRedirect(reverse('settingsMetalprotec:settingsMetalprotec'))