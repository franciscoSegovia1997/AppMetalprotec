from django.shortcuts import render
from .models import productSystem, storeSystem, storexproductSystem
from decimal import Decimal, DecimalException,getcontext
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from stockManagment.models import incomingItemsRegisterInfo
import datetime
from settingsMetalprotec.models import endpointSystem

getcontext().prec = 10

# Create your views here.
def productsMetalprotec(request):
    if request.method == 'POST':
        if 'newProduct' in request.POST:
            nameProduct=request.POST.get('nameProduct')
            codeProduct=request.POST.get('codeProduct')
            codeSunatProduct=request.POST.get('codeSunatProduct')
            categoryProduct=request.POST.get('categoryProduct')
            subCategoryProduct=request.POST.get('subCategoryProduct')
            measureUnit=request.POST.get('measureUnit')
            weightProduct=request.POST.get('weightProduct')
            currencyProduct=request.POST.get('currencyProduct')
            pvnIGV = str(Decimal('%.2f' % Decimal(request.POST.get('pvnIGV'))))
            pvcIGV = str(Decimal('%.2f' % (Decimal(pvnIGV)*Decimal(1.18))))
            pcnIGV = str(Decimal('%.2f' % Decimal(request.POST.get('pcnIGV'))))
            pccIGV = str(Decimal('%.2f' % (Decimal(pcnIGV)*Decimal(1.18))))
            kitProduct = request.POST.get('kitProduct')
            if kitProduct == 'on':
                kitProduct = 'ON'
            else:
                kitProduct = 'OFF'
            endpointProduct=request.user.extendeduser.endpointUser

            productObjectCreated = productSystem.objects.create(
                nameProduct=nameProduct,
                codeProduct=codeProduct,
                codeSunatProduct=codeSunatProduct,
                categoryProduct=categoryProduct,
                subCategoryProduct=subCategoryProduct,
                measureUnit=measureUnit,
                weightProduct=weightProduct,
                currencyProduct=currencyProduct,
                pvnIGV=pvnIGV,
                pvcIGV=pvcIGV,
                pcnIGV=pcnIGV,
                pccIGV=pccIGV,
                kitProduct=kitProduct,
                endpointProduct=endpointProduct,
            )

            allStoreSystem = storeSystem.objects.filter(endpointStore=request.user.extendeduser.endpointUser)
            for storeInfo in allStoreSystem:
                storexproductSystem.objects.create(
                    quantityProduct='0',
                    asociatedProduct=productObjectCreated,
                    asociatedStore=storeInfo,
                )
            return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))


    return render(request,'productsMetalprotec.html',{
        'productsSystem':productSystem.objects.filter(endpointProduct=request.user.extendeduser.endpointUser).order_by('id'),
        'storesSystem':storeSystem.objects.filter(endpointStore=request.user.extendeduser.endpointUser).order_by('id'),
    })

@login_required(login_url='/')
def deleteProduct(request):
    if request.method == 'POST':
        deleteIdProduct = request.POST.get('deleteIdProduct')
        deleteProduct = productSystem.objects.get(id=deleteIdProduct)
        deleteProduct.delete()
        return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))
    
@login_required(login_url='/')
def getProductData(request):
    idProduct=request.GET.get('idProduct')
    editProduct=productSystem.objects.get(id=idProduct)
    return JsonResponse({
        'editNameProduct':editProduct.nameProduct,
        'editMeasureUnit':editProduct.measureUnit,
        'editCodeProduct':editProduct.codeProduct,
        'editCodeSunatProduct':editProduct.codeSunatProduct,
        'editCategoryProduct':editProduct.categoryProduct,
        'editSubCategoryProduct':editProduct.subCategoryProduct,
        'editPvnIGV':editProduct.pvnIGV,
        'editPcnIGV':editProduct.pcnIGV,
        'editWeightProduct':editProduct.weightProduct,
        'editCurrencyProduct':editProduct.currencyProduct,
        'editKit':editProduct.kitProduct,
    })

@login_required(login_url='/')
def updateProduct(request):
    if request.method == 'POST':
        editIdProduct=request.POST.get('editIdProduct')
        editNameProduct=request.POST.get('editNameProduct')
        editMeasureUnit=request.POST.get('editMeasureUnit')
        editCodeProduct=request.POST.get('editCodeProduct')
        editCodeSunatProduct=request.POST.get('editCodeSunatProduct')
        editCategoryProduct=request.POST.get('editCategoryProduct')
        editSubCategoryProduct=request.POST.get('editSubCategoryProduct')
        editPvnIGV=str(Decimal('%.2f' % Decimal(request.POST.get('editPvnIGV'))))
        editPvcIGV=str(Decimal('%.2f' % (Decimal(editPvnIGV)*Decimal(1.18))))
        editPcnIGV=str(Decimal('%.2f' % Decimal(request.POST.get('editPcnIGV'))))
        editPccIGV=str(Decimal('%.2f' % (Decimal(editPcnIGV)*Decimal(1.18))))
        editWeightProduct=request.POST.get('editWeightProduct')
        editCurrencyProduct=request.POST.get('editCurrencyProduct')
        editKit = request.POST.get('editKit')

        if editKit == 'on':
            editKit = 'ON'
        else:
            editKit = 'OFF'

        editProduct=productSystem.objects.get(id=editIdProduct)
        editProduct.nameProduct=editNameProduct
        editProduct.measureUnit=editMeasureUnit
        editProduct.codeProduct=editCodeProduct
        editProduct.codeSunatProduct=editCodeSunatProduct
        editProduct.categoryProduct=editCategoryProduct
        editProduct.subCategoryProduct=editSubCategoryProduct
        editProduct.pvnIGV=editPvnIGV
        editProduct.pvcIGV=editPvcIGV
        editProduct.pcnIGV=editPcnIGV
        editProduct.pccIGV=editPccIGV
        editProduct.weightProduct=editWeightProduct
        editProduct.currencyProduct=editCurrencyProduct
        editProduct.kitProduct = editKit
        editProduct.save()

        if editKit == 'OFF':
            editProduct.kitInfo = []
            editProduct.save()
        return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))

@login_required(login_url='/')
def getProductStock(request):
    idProduct=request.GET.get('idProduct')
    stockProduct = productSystem.objects.get(id=idProduct)
    stockStoreProduct = []
    for stock in stockProduct.storexproductsystem_set.all():
        stockStoreProduct.append([stock.asociatedStore.nameStore,stock.quantityProduct])
    print(stockStoreProduct)
    return JsonResponse({
        'stockStoreProduct':stockStoreProduct,
    })

@login_required(login_url='/')
def addStockProduct(request):
    if request.method == 'POST':
        addStockIdProduct = request.POST.get('addStockIdProduct')
        addStockIdStore = request.POST.get('addStockIdStore')
        addStockQt = str(Decimal('%.2f' % Decimal(request.POST.get('addStockQt'))))
        addStockProduct=productSystem.objects.get(id=addStockIdProduct)
        addStockStore=storeSystem.objects.get(id=addStockIdStore)
        if checkStockExist(addStockProduct,addStockStore):
            stockEdit = storexproductSystem.objects.filter(asociatedProduct=addStockProduct).get(asociatedStore=addStockStore)
            lastStock = stockEdit.quantityProduct
            stockEdit.quantityProduct = str(Decimal('%.2f' % Decimal(Decimal(stockEdit.quantityProduct) + Decimal(addStockQt))))
            stockEdit.save()
            newStock = stockEdit.quantityProduct
            typeIncoming = 'INGRESO-PRODUCTOS'
            dateIncoming = datetime.datetime.today()
            productCode = addStockProduct.codeProduct
            nameStore = addStockStore.nameStore
            quantityProduct = addStockQt
            referenceIncome = 'INGRESO'
            asociatedUserData = request.user
            asociatedProduct = addStockProduct
            asociatedStoreData = addStockStore
            endpointIncoming = request.user.extendeduser.endpointUser
            incomingItemsRegisterInfo.objects.create(
                typeIncoming=typeIncoming,
                dateIncoming=dateIncoming,
                productCode=productCode,
                nameStore=nameStore,
                quantityProduct=quantityProduct,
                lastStock=lastStock,
                newStock=newStock,
                referenceIncome=referenceIncome,
                asociatedUserData=asociatedUserData,
                asociatedProduct=asociatedProduct,
                asociatedStoreData=asociatedStoreData,
                endpointIncoming=endpointIncoming
            )
        else:
            storexproductSystem.objects.create(
                asociatedProduct=addStockProduct,
                asociatedStore=addStockStore,
                quantityProduct=addStockQt,
            )
        return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))

def checkStockExist(productInfo,storeInfo):
    stockCheck = productInfo.storexproductsystem_set.all().filter(asociatedStore=storeInfo)
    if len(stockCheck) == 0:
        return False
    else:
        return True
    
def importProductsData(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))

def getProductKit(request):
    arrayKit = []
    idProduct = request.GET.get('idProduct')
    productObject = productSystem.objects.get(id=idProduct)
    print(productObject.kitInfo)
    if productObject.kitInfo is not None:
        i = 0
        for productInformation in productObject.kitInfo:
            arrayKit.append([productSystem.objects.get(id=productInformation[0]).codeProduct,productInformation[1]])
    else:
        arrayKit = []
    return JsonResponse({
        'arrayKit':arrayKit
    })

def addProductKit(request):
    if request.method == 'POST':
        idProductKit = request.POST.get('idProductKit')
        idNewProduct = request.POST.get('newProductKit')
        qtNewProduct = request.POST.get('qtProductKit')

        productObject = productSystem.objects.get(id=idProductKit)

        if productObject.kitInfo is not None:
            try:
                productObject.kitInfo.append([idNewProduct,qtNewProduct])
                productObject.save()
            except:
                productObject.kitInfo.append(['NOCODE',qtNewProduct])
                productObject.save()
        else:
            productObject.kitInfo = []
            productObject.save()
            try:
                productObject.kitInfo.append([idNewProduct,qtNewProduct])
                productObject.save()
            except:
                productObject.kitInfo.append(['NOCODE',qtNewProduct])
                productObject.save()
        
        return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))

def changeStore(request):
    if request.method == 'POST':
        idProductInfo = request.POST.get('changeStoreProduct')
        idEndpoint = request.POST.get('endpointStoreProduct')
        qtStock = request.POST.get('stockMove')
        productoActual = productSystem.objects.get(id=idProductInfo)
        endpointDestino = endpointSystem.objects.get(id=idEndpoint)
        productoDestino = productSystem.objects.filter(endpointProduct=endpointDestino).filter(codeProduct=productoActual.codeProduct)
        if len(productoDestino == 1):
            productoFinal = productoDestino[0]
            stockFinal = productoFinal.storexproductsystem_set.all()[0]
            stockInicial = productoActual.storexproductsystem_set.all()[0]
            stockMove = str(Decimal('%.2f' % Decimal(qtStock)))
            stockInicial.quantityProduct = str(Decimal('%.2f' % Decimal(Decimal(stockInicial.quantityProduct) - Decimal(stockMove))))
            stockInicial.save()
            stockFinal.quantityProduct = str(Decimal('%.2f' % Decimal(Decimal(stockFinal.quantityProduct) + Decimal(stockMove))))
            stockFinal.save()
        else:
            pass
        return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))
