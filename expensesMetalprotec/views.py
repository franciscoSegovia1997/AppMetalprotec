from django.shortcuts import render
from .models import departmentCost, categoryCost, divisionCost,costRegister, boxRegister, cashIncome, ordenCompraMetalprotec
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
import datetime
from productsMetalprotec.models import productSystem
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from decimal import Decimal, DecimalException,getcontext

getcontext().prec = 10

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
    return render(request,'purchaseOrder.html',{
        'totalPurchaseOrder':ordenCompraMetalprotec.objects.filter(endpointOrden=request.user.extendeduser.endpointUser)
    })

def deleteOrden(request,ind):
    ordenCompraMetalprotec.objects.get(id=ind).delete()
    return HttpResponseRedirect(reverse('expensesMetalprotec:purchaseOrder'))

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

def newPurchaseOrder(request):
    return render(request,'newPurchaseOrder.html',{
        'productsSystem': productSystem.objects.all().order_by('id')
    })

def getProductInfoExpenses(request,ind):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            producto_informacion = productSystem.objects.get(id=ind)
            return JsonResponse(
                {
                    'nombre':producto_informacion.nameProduct,
                    'codigo':producto_informacion.codeProduct,
                    'unidad_med':producto_informacion.measureUnit,
                    'pv_sinIGV':producto_informacion.pvnIGV,
                    'moneda':producto_informacion.currencyProduct,
                    'pc_sinIGV':producto_informacion.pcnIGV
                })
        return JsonResponse({'status': 'Invalid request'}, status=200)
    else:
        return HttpResponseBadRequest('Invalid request')

def createOrden(request):
    if request.method == 'POST':
        data = json.load(request)
        rucProveedor = data.get('rucProveedor')
        fechaOrden = data.get('fechaOrden')
        condicionOrden = data.get('condicionOrden')
        codigoOrden = data.get('codigoOrden')
        direccionProveedor = data.get('direccionProveedor')
        nombreProveedor = data.get('nombreProveedor')
        ciudadCliente = data.get('ciudadCliente')
        destinoCliente = data.get('destinoCliente')
        atencionCliente = data.get('atencionCliente')
        monedaOrden = data.get('monedaOrden')
        productosOrden = data.get('productos')
        tcCompraOrden = data.get('tcCompraOrden')
        tcVentaOrden = data.get('tcVentaOrden')
        mostrarDescuento = data.get('mostrarDescuento')
        mostrarVU = data.get('mostrarVU')
        endpointOrden = request.user.extendeduser.endpointUser
        if fechaOrden == '':
            fechaEmision = datetime.datetime.today()
        else:
            fechaEmision = datetime.datetime.strptime(fechaOrden,'%Y-%m-%d')
        ordenCompraMetalprotec.objects.create(
            rucProveedor=rucProveedor,
            fechaEmision=fechaEmision,
            condicionOrden=condicionOrden,
            codigoOrden=codigoOrden,
            direccionProveedor=direccionProveedor,
            nombreProveedor=nombreProveedor,
            ciudadCliente=ciudadCliente,
            destinoCliente=destinoCliente,
            atencionCliente=atencionCliente,
            monedaOrden=monedaOrden,
            productosOrden=productosOrden,
            tcCompraOrden=tcCompraOrden,
            tcVentaOrden=tcVentaOrden,
            mostrarDescuento=mostrarDescuento,
            mostrarVU=mostrarVU,
            endpointOrden=endpointOrden
        )
        return JsonResponse({
            'resp':'200'
        })

def downloadOrden(request,ind):
    #Se proceden a generar las paginas del documento
    #Generacion del documento
    pdf_name = 'orden_generada.pdf'
    can = canvas.Canvas(pdf_name,pagesize=A4)

    #Obtencion de la informacion
    orden_info = ordenCompraMetalprotec.objects.get(id=ind)
    total_precio = Decimal(0.0000)

    #Generacion del membrete superior derecho
    can.setStrokeColorRGB(0,0,1)
    lista_x = [400,580]
    lista_y = [720,815]
    can.grid(lista_x,lista_y)
    can.setFillColorRGB(0,0,0)
    can.setFont('Helvetica',12)
    can.drawString(440,785,'RUC: 20541628631')
    can.setFont('Helvetica-Bold',12)
    can.drawString(430,765,'ORDEN DE COMPRA')
    can.setFont('Helvetica',12)
    can.drawString(460,745,str(orden_info.codigoOrden))

    #Generacion del logo
    can.drawImage('./static/images/logoMetalprotecBase.png',10,705,width=120,height=120)
    
    #Informacion del remitente
    can.setFont('Helvetica-Bold',10)
    can.drawString(25,705,'METALPROTEC')
    can.setFont('Helvetica',7)
    can.drawString(25,695,'LT 39 MZ. J4 URB. PASEO DEL MAR - ÁNCASH SANTA NUEVO CHIMBOTE')
    can.drawString(25,687,'Teléfono: (043) 282752')
    #can.drawString(25,679,'E-Mail: contabilidad@metalprotec.pe')

    #Generacion de la linea de separacion
    can.line(25,670,580,670)

    #Generacion de los datos del cliente
    can.setFont('Helvetica-Bold',7)
    can.drawString(25,660,'RUC :')
    can.drawString(25,650,'Señores :')
    can.drawString(25,640,'Direccion :')
    can.drawString(25,630,'Moneda :')
    can.drawString(400,660,'Nro Documento :')
    can.drawString(400,650,'Fecha de emisión :')
    can.drawString(400,640,'Condicion :')

    can.setFont('Helvetica',7)
    can.drawString(120,660,str(orden_info.rucProveedor))    
    can.drawString(120,650,str(orden_info.nombreProveedor))    
    can.drawString(120,640,str(orden_info.direccionProveedor))
    can.drawString(120,630,str(orden_info.monedaOrden))
    can.drawString(500,660,str(orden_info.codigoOrden))
    can.drawString(500,650,str(orden_info.fechaEmision.strftime('%d-%m-%Y')))
    can.drawString(500,640,str(orden_info.condicionOrden))

    #Linea de separacion con los datos del vendedor
    can.line(25,620,580,620)

    #Datos del vendedor
    can.setFont('Helvetica-Bold',7)
    can.drawString(25,610,'Atencion:')
    can.drawString(25,600,'Ciudad de destino:')
    can.drawString(25,590,'Direccion de entrega:')

    can.setFont('Helvetica',7)
    can.drawString(120,610,str(orden_info.atencionCliente))
    can.drawString(120,600,str(orden_info.ciudadCliente))    
    can.drawString(120,590,str(orden_info.destinoCliente))

    #Aqui se ponen las cabeceras

    can.setStrokeColorRGB(0,0,1)
    can.setFillColorRGB(0,0,0)
    #Campos en cabecera
    lista_x = [25,580]
    lista_y = [550,565]
    can.setFillColorRGB(0,0,1)
    can.rect(25,550,555,15,fill=1)

    #Valores iniciales
    lista_x = [25,55,110,310,360,410,460,530]
    lista_y = [550,565]
    #Ingreso de campo cantidad
    can.setFillColorRGB(1,1,1)
    can.setFont('Helvetica-Bold',7)
    can.drawString(lista_x[0] + 5, lista_y[0] + 3,'Cant.')
    can.setFont('Helvetica',7)
    can.setFillColorRGB(0,0,0)
    lista_y = [lista_y[0] - 16,lista_y[1] - 16]
    for producto in orden_info.productosOrden:
        can.drawRightString(lista_x[0] + 25,lista_y[0] + 3,str("{:.2f}".format(round(float(producto[5]),2))))
        lista_y = [lista_y[0] - 16,lista_y[1] - 16]
    
    
    #Valores iniciales
    lista_y = [550,565]
    #Ingreso de campo de código de producto
    can.setFillColorRGB(1,1,1)
    can.setFont('Helvetica-Bold',7)
    can.drawString(lista_x[1] + 5, lista_y[0] + 3,'Código')
    can.setFont('Helvetica',7)
    can.setFillColorRGB(0,0,0)
    lista_y = [lista_y[0] - 16,lista_y[1] - 16]
    for producto in orden_info.productosOrden:
        can.drawString(lista_x[1] + 5,lista_y[0] + 3,producto[2])
        lista_y = [lista_y[0] - 16,lista_y[1] - 16]

    #Valores iniciales
    lista_y = [550,565]
    #Ingreso de campo de descripcion de producto
    can.setFillColorRGB(1,1,1)
    can.setFont('Helvetica-Bold',7)
    can.drawString(lista_x[2] + 5, lista_y[0] + 3,'Descripción')
    can.setFont('Helvetica',7)
    can.setFillColorRGB(0,0,0)
    lista_y = [lista_y[0] - 16,lista_y[1] - 16]
    for producto in orden_info.productosOrden:
        can.drawString(lista_x[2] + 5,lista_y[0] + 3,producto[1])
        lista_y = [lista_y[0] - 16,lista_y[1] - 16]

    #Valores iniciales
    lista_y = [550,565]
    #Ingreso de campo de descuento del producto
    can.setFillColorRGB(1,1,1)
    can.setFont('Helvetica-Bold',7)
    can.drawString(lista_x[4] - 3, lista_y[0] + 3,'V.U')
    can.setFont('Helvetica',7)
    can.setFillColorRGB(0,0,0)
    lista_y = [lista_y[0] - 16,lista_y[1] - 16]
    for producto in orden_info.productosOrden:
        v_producto = Decimal(0.0000)
        if orden_info.monedaOrden == 'SOLES':
            if producto[3] == 'DOLARES':
                v_producto = Decimal('%.2f' % (Decimal(Decimal(producto[4])*Decimal(orden_info.tcCompraOrden))*Decimal(Decimal(1.00) - Decimal((Decimal(producto[6])/100)))))
            if producto[3] == 'SOLES':
                v_producto = Decimal(producto[4])*Decimal(Decimal(1.00) - Decimal((Decimal(producto[6])/100)))
        if orden_info.monedaOrden == 'DOLARES':
            if producto[3] == 'SOLES':
                v_producto = Decimal('%.2f' % (Decimal(producto[4])/Decimal(orden_info.tcCompraOrden)))*Decimal(Decimal(1.00) - Decimal((Decimal(producto[6])/100)))
            if producto[3] == 'DOLARES':
                v_producto = Decimal(producto[4])*Decimal(Decimal(1.00) - Decimal((Decimal(producto[6])/100)))
        can.drawRightString(lista_x[4] + 20,lista_y[0] + 3,"{:,}".format(Decimal('%.2f' % v_producto)))
        lista_y = [lista_y[0] - 16,lista_y[1] - 16]
    
    if orden_info.mostrarVU == '1' and orden_info.mostrarDescuento == '1':
        lista_x[5] = 410
        lista_x[6] = 460
    
    if orden_info.mostrarVU == '1' and orden_info.mostrarDescuento == '0':
        lista_x[5] = 410
        lista_x[6] = 460

    if orden_info.mostrarVU == '0' and orden_info.mostrarDescuento == '1':
        lista_x[5] = 460
        lista_x[6] = 410
    
    if orden_info.mostrarVU == '0' and orden_info.mostrarDescuento == '0':
        lista_x[5] = 410
        lista_x[6] = 460
    
    if orden_info.mostrarVU == '1':
        #Valores iniciales
        lista_y = [550,565]
        #Ingreso de campo de unidad de medida de producto
        can.setFillColorRGB(1,1,1)
        can.setFont('Helvetica-Bold',7)
        can.drawString(lista_x[5] - 5, lista_y[0] + 3,'V.U sin IGV')
        can.setFont('Helvetica',7)
        can.setFillColorRGB(0,0,0)
        lista_y = [lista_y[0] - 16,lista_y[1] - 16]
        for producto in orden_info.productosOrden:
            if orden_info.monedaOrden == 'SOLES':
                if producto[3] == 'DOLARES':
                    vu_producto = Decimal(producto[4])*Decimal(orden_info.tcCompraOrden)
                if producto[3] == 'SOLES':
                    vu_producto = Decimal(producto[4])
            if orden_info.monedaOrden == 'DOLARES':
                if producto[3] == 'SOLES':
                    vu_producto = (Decimal(producto[4])/Decimal(orden_info.tcCompraOrden))
                if producto[3] == 'DOLARES':
                    vu_producto = Decimal(producto[4])
            can.drawRightString(lista_x[5] + 20,lista_y[0] + 3,"{:,}".format(Decimal('%.2f' % vu_producto)))
            lista_y = [lista_y[0] - 16,lista_y[1] - 16]
    
    

    if orden_info.mostrarDescuento == '1':
        #Valores iniciales
        lista_y = [550,565]
        #Ingreso de campo de descuento del producto
        can.setFillColorRGB(1,1,1)
        can.setFont('Helvetica-Bold',7)
        can.drawString(lista_x[6] + 5, lista_y[0] + 3,'Dsct.')
        can.setFont('Helvetica',7)
        can.setFillColorRGB(0,0,0)
        lista_y = [lista_y[0] - 16,lista_y[1] - 16]
        for producto in orden_info.productosOrden:
            can.drawRightString(lista_x[6] + 20,lista_y[0] + 3,producto[6] + '%')
            lista_y = [lista_y[0] - 16,lista_y[1] - 16]

    #Valores iniciales
    lista_y = [550,565]
    #Ingreso de campo de valor de venta del producto
    can.setFillColorRGB(1,1,1)
    can.setFont('Helvetica-Bold',7)
    can.drawString(lista_x[7] + 5, lista_y[0] + 3,'Valor Venta')
    can.setFont('Helvetica',7)
    can.setFillColorRGB(0,0,0)
    lista_y = [lista_y[0] - 16,lista_y[1] - 16]
    for producto in orden_info.productosOrden:
        if orden_info.monedaOrden == 'SOLES':
            if producto[3] == 'DOLARES':
                v_producto = Decimal('%.2f' % (Decimal(producto[4])*Decimal(orden_info.tcCompraOrden)))*Decimal(Decimal(1.00) - Decimal((Decimal(producto[6])/100)))
                v_producto = Decimal('%.2f' % (v_producto*Decimal(producto[5])))
            if producto[3] == 'SOLES':
                v_producto = Decimal(producto[4])*Decimal(Decimal(1.00) - Decimal((Decimal(producto[6])/100)))
                v_producto = Decimal('%.2f' % (v_producto*Decimal(producto[5])))
        if orden_info.monedaOrden == 'DOLARES':
            if producto[3] == 'SOLES':
                v_producto = Decimal('%.2f' % (Decimal(producto[4])/Decimal(orden_info.tcCompraOrden)))*Decimal(Decimal(1.00) - Decimal((Decimal(producto[6])/100)))
                v_producto = Decimal('%.2f' % (v_producto*Decimal(producto[5])))
            if producto[3] == 'DOLARES':
                v_producto = Decimal(producto[4])*Decimal(Decimal(1.00) - Decimal((Decimal(producto[6])/100)))
                v_producto = Decimal('%.2f' % (v_producto*Decimal(producto[5])))
        #v_producto = round(v_producto,2)
        can.drawRightString(lista_x[7] + 45,lista_y[0] + 3,"{:,}".format(Decimal('%.2f' % Decimal(v_producto))))
        lista_y = [lista_y[0] - 16,lista_y[1] - 16]
        total_precio = Decimal(total_precio) + Decimal(v_producto)

    #Linea de separacion con los datos finales
    can.line(25,lista_y[1],580,lista_y[1])
    #Prueba de impresion

    #Linea final de separacion
    can.line(25,25,580,25)

    #Esta seccion solo va en la hoja final de los productos
    #Impresion de total venta
    can.drawRightString(480,lista_y[0]+4,'Total Venta Grabada')
    if orden_info.monedaOrden == 'SOLES':
        can.drawRightString(490,lista_y[0]+4,'S/')
    else:
        can.drawRightString(490,lista_y[0]+4,'$')
    can.drawRightString(lista_x[7]+45,lista_y[0]+4,"{:,}".format(Decimal('%.2f' % total_precio)))
    lista_y = [lista_y[0] - 15,lista_y[1] - 15]

    #Linea de separacion
    can.line(480,lista_y[1],580,lista_y[1])

    #Impresion de total IGV
    igv_precio = Decimal('%.2f' % total_precio)*Decimal(0.18)
    can.drawRightString(480,lista_y[0]+4,'Total IGV')
    if orden_info.monedaOrden == 'SOLES':
        can.drawRightString(490,lista_y[0]+4,'S/')
    else:
        can.drawRightString(490,lista_y[0]+4,'$')
    can.drawRightString(lista_x[7]+45,lista_y[0]+4,"{:,}".format(Decimal('%.2f' % igv_precio)))
    lista_y = [lista_y[0] - 15,lista_y[1] - 15]

    #Linea de separacion
    can.line(480,lista_y[1],580,lista_y[1])

    #Impresion de importe total
    precio_final = Decimal('%.2f' % total_precio)*Decimal(1.18)
    can.drawRightString(480,lista_y[0]+4,'Importe Total de la Venta')
    if orden_info.monedaOrden == 'SOLES':
        can.drawRightString(490,lista_y[0]+4,'S/')
    else:
        can.drawRightString(490,lista_y[0]+4,'$')
    can.drawRightString(lista_x[7]+45,lista_y[0]+4,"{:,}".format(Decimal('%.2f' % Decimal(precio_final))))
    lista_y = [lista_y[0] - 15,lista_y[1] - 15]

    #Linea de separacion
    can.line(480,lista_y[1],580,lista_y[1])

    #Dibujo del cuadrado para firma

    can.setStrokeColorRGB(0,0,1)
    lista_x = [25,580]
    lista_y = [30,80]
    can.grid(lista_x,lista_y)
    can.setFillColorRGB(0,0,0)

    can.setFont('Helvetica',9)
    can.drawString(100,35,'Revisado por gerencia')

    #Generacion de la firma
    can.drawImage('./static/images/firmaOrdenCompra.png',90,30,width=113,height=51,mask='auto')

    #Linea de separacion con los datos finales
    can.line(25,lista_y[1],580,lista_y[1])
    can.save()

    nombre_doc = str(orden_info.codigoOrden) + '.pdf'
    response = HttpResponse(open('orden_generada.pdf','rb'),content_type='application/pdf')
    nombre = 'attachment; ' + 'filename=' + nombre_doc
    response['Content-Disposition'] = nombre
    return response


def editOrder(request,ind):
    orden_editar = ordenCompraMetalprotec.objects.get(id=ind)
    return render(request,'editPurchaseOrder.html',{
        'orden':orden_editar,
        'productsSystem': productSystem.objects.all().order_by('id')
    })

def updateOrder(request,ind):
    orden_editar = ordenCompraMetalprotec.objects.get(id=ind)
    if request.method == 'POST':
        data = json.load(request)
        rucProveedor = data.get('rucProveedor')
        fechaOrden = data.get('fechaOrden')
        condicionOrden = data.get('condicionOrden')
        codigoOrden = data.get('codigoOrden')
        direccionProveedor = data.get('direccionProveedor')
        nombreProveedor = data.get('nombreProveedor')
        ciudadCliente = data.get('ciudadCliente')
        destinoCliente = data.get('destinoCliente')
        atencionCliente = data.get('atencionCliente')
        monedaOrden = data.get('monedaOrden')
        productosOrden = data.get('productos')
        tcCompraOrden = data.get('tcCompraOrden')
        tcVentaOrden = data.get('tcVentaOrden')
        mostrarDescuento = data.get('mostrarDescuento')
        mostrarVU = data.get('mostrarVU')
        if fechaOrden == '':
            fechaEmision = datetime.datetime.today()
        else:
            fechaEmision = datetime.datetime.strptime(fechaOrden,'%Y-%m-%d')
        
        orden_editar.rucProveedor = rucProveedor
        orden_editar.fechaEmision = fechaEmision
        orden_editar.condicionOrden = condicionOrden
        orden_editar.codigoOrden = codigoOrden
        orden_editar.direccionProveedor = direccionProveedor
        orden_editar.nombreProveedor = nombreProveedor
        orden_editar.ciudadCliente = ciudadCliente
        orden_editar.destinoCliente = destinoCliente
        orden_editar.atencionCliente = atencionCliente
        orden_editar.monedaOrden = monedaOrden
        orden_editar.productosOrden = productosOrden
        orden_editar.tcCompraOrden = str(tcCompraOrden)
        orden_editar.tcVentaOrden = str(tcVentaOrden)
        orden_editar.mostrarDescuento = mostrarDescuento
        orden_editar.mostrarVU = mostrarVU
        orden_editar.save()
        time.sleep(0.5)
        return JsonResponse({
            'resp':'ok'
        })