from django.shortcuts import render
from .models import incomingItemsRegisterInfo,outcomingItemsRegisterInfo,stockTakingData, infoStockTaking
from productsMetalprotec.models import storeSystem, productSystem
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Create your views here.
def incomingItems(request):
    return render(request,'incomingItems.html',{
        'incomingRegistersData':incomingItemsRegisterInfo.objects.filter(endpointIncoming=request.user.extendeduser.endpointUser)
    })

def outcomingItems(request):
    return render(request,'outcomingItems.html',{
        'outcomingRegistersData':outcomingItemsRegisterInfo.objects.filter(endpointOutcoming=request.user.extendeduser.endpointUser)
    })

def stockTaking(request):
    if request.method == 'POST':
        selectedStore = request.POST.get('selectedStore')
        asociatedStoreData = storeSystem.objects.get(id=selectedStore)
        endpointInfo = request.user.extendeduser.endpointUser
        totalProductsInfo = productSystem.objects.filter(endpointProduct=endpointInfo)
        dateStockTaking=datetime.datetime.today()
        asociatedStockTaking = stockTakingData.objects.create(
            dateStockTaking=dateStockTaking,
            stateStockTaking='REVISION',
            storeStokTaking=asociatedStoreData.nameStore,
            asociatedUserData=request.user,
            asociatedStoreData=asociatedStoreData,
            endpointStockTaking=request.user.extendeduser.endpointUser,
        )
        for asociatedProsductInfo in totalProductsInfo:
            infoData = asociatedProsductInfo.storexproductsystem_set.all().filter(asociatedStore=asociatedStoreData)
            if len(infoData)==1:
                if float(infoData[0].quantityProduct) > 0:
                    dataStockTakingInfo = [asociatedProsductInfo.nameProduct,asociatedProsductInfo.codeProduct,infoData[0].quantityProduct,asociatedProsductInfo.pcnIGV,asociatedProsductInfo.pvnIGV]
                    infoStockTaking.objects.create(
                        asociatedStockTaking=asociatedStockTaking,
                        asociatedProsductInfo=asociatedProsductInfo,
                        dataStockTakingInfo=dataStockTakingInfo,
                    )
        codeStockTaking = str(asociatedStockTaking.id)
        while len(codeStockTaking) < 4:
            codeStockTaking = '0' + codeStockTaking
        codeStockTaking = f'INV-{codeStockTaking}'
        asociatedStockTaking.codeStockTaking = codeStockTaking
        asociatedStockTaking.save()
        return HttpResponseRedirect(reverse('stockManagment:stockTaking'))
    return render(request,'stockTaking.html',{
        'stockTakingRegistersData':stockTakingData.objects.filter(endpointStockTaking=request.user.extendeduser.endpointUser),
        'storeSystemInfo':storeSystem.objects.filter(endpointStore=request.user.extendeduser.endpointUser)
    })

def deleteStockTaking(request,idStockTaking):
    stockTakingData.objects.get(id=idStockTaking).delete()
    return HttpResponseRedirect(reverse('stockManagment:stockTaking'))

def downloadStockTaking(request,idStockTaking):
    #Generacion del documento
    pdf_name = 'stockTakingInfo.pdf'
    can = canvas.Canvas(pdf_name,pagesize=A4)

    #Obtencion de la informacion
    stockTakingInfo = stockTakingData.objects.get(id=idStockTaking)
    totalProductsInStock = stockTakingInfo.infostocktaking_set.all()
    groupQuantity = [totalProductsInStock[x:x+40] for x in range(0,len(totalProductsInStock),40)]
    indicatorGroup = 0
    while indicatorGroup < len(groupQuantity):
        can.setFont('Helvetica',24)
        can.drawString(25,800,'Stock de productos')
        can.drawString(25,770,'Almacen : ')
        can.drawString(150,770,stockTakingInfo.storeStokTaking)
        can.setFont('Helvetica',12)
        lista_x = [25,50,100,310,360,410,460,530]
        lista_y = [730,745]
        #Ingreso de campo cantidad
        can.setFillColorRGB(0,0,0)
        can.setFont('Helvetica-Bold',7)
        can.drawString(lista_x[0] + 5, lista_y[0] + 3,'Producto')
        can.drawString(lista_x[4] + 5, lista_y[0] + 3,'Stock')
        can.setFont('Helvetica',7)
        can.setFillColorRGB(0,0,0)
        lista_y = [lista_y[0] - 16,lista_y[1] - 16]
        counter_stock = 0
        for productInfo in groupQuantity[indicatorGroup]:
            can.drawString(lista_x[0] + 5,lista_y[0] + 3,str(productInfo.dataStockTakingInfo[0]))
            can.drawRightString(lista_x[4] + 20,lista_y[0] + 3,str(productInfo.dataStockTakingInfo[2]))
            lista_y = [lista_y[0] - 16,lista_y[1] - 16]
            counter_stock = counter_stock + 1
        indicatorGroup = indicatorGroup + 1
        if len(groupQuantity) > indicatorGroup:
            can.showPage()
    if len(groupQuantity) == 0:
        can.setFont('Helvetica',24)
        can.drawString(25,800,'Stock de productos')
        can.drawString(25,770,'Almacen : ')
        can.drawString(150,770,stockTakingInfo.storeStokTaking)
        can.setFont('Helvetica',12)
        lista_x = [25,50,100,310,360,410,460,530]
        lista_y = [730,745]
        can.showPage()
    can.save()
    nombre_doc = str(stockTakingInfo.codeStockTaking) + '.pdf'
    response = HttpResponse(open('stockTakingInfo.pdf','rb'),content_type='application/pdf')
    nombre = 'attachment; ' + 'filename=' + nombre_doc
    response['Content-Disposition'] = nombre
    return response