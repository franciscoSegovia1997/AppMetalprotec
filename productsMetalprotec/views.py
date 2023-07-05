from django.shortcuts import render
from .models import productSystem, storeSystem, storexproductSystem
from decimal import Decimal, DecimalException,getcontext
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
            endpointProduct=request.user.extendeduser.endpointUser

            productSystem.objects.create(
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
                endpointProduct=endpointProduct,
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
        editProduct.save()
        return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))

@login_required(login_url='/')
def getProductStock(request):
    idProduct=request.GET.get('idProduct')
    stockProduct = productSystem.objects.get(id=idProduct)
    stockStoreProduct = []
    for stock in stockProduct.storexproductsystem_set.all():
        stockStoreProduct.append([stock.asociatedStore.nameStore,stock.quatityProduct])
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
            stockEdit.quatityProduct = str(Decimal('%.2f' % Decimal(Decimal(stockEdit.quatityProduct) + Decimal(addStockQt))))
            stockEdit.save()
        else:
            storexproductSystem.objects.create(
                asociatedProduct=addStockProduct,
                asociatedStore=addStockStore,
                quatityProduct=addStockQt,
            )
        return HttpResponseRedirect(reverse('productsMetalprotec:productsMetalprotec'))

def checkStockExist(productInfo,storeInfo):
    stockCheck = productInfo.storexproductsystem_set.all().filter(asociatedStore=storeInfo)
    if len(stockCheck) == 0:
        return False
    else:
        return True