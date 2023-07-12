from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from clientsMetalprotec.models import clientSystem
from productsMetalprotec.models import productSystem
from django.contrib.auth.models import User
from servicesMetalprotec.models import serviceSystem
from usersMetalprotec.models import extendedUser
from settingsMetalprotec.models import endpointSystem
from .models import quotationSystem, quotationClientData, quotationProductData, quotationSellerData, quotationServiceData, guideSystem, creditNoteSystem, invoiceSystem, billSystem
from dateutil.parser import parse
import json
import datetime

# Create your views here.
def quotationsMetalprotec(request):
    return render(request,'quotationsMetalprotec.html',{
        'quotationsSystem':quotationSystem.objects.filter(endpointQuotation=request.user.extendeduser.endpointUser).order_by('id')
    })

def guidesMetalprotec(request):
    return render(request,'guidesMetalprotec.html',{
        'guidesSystem':guideSystem.objects.filter(endpointGuide=request.user.extendeduser.endpointUser)
    })

def billsMetalprotec(request):
    return render(request,'billsMetalprotec.html',{
        'billsSystem':billSystem.objects.filter(endpointBill=request.user.extendeduser.endpointUser)
    })

def invoicesMetalprotec(request):
    return render(request,'invoicesMetalprotec.html')

def creditNotesMetalprotec(request):
    return render(request,'creditNotesMetalprotec.html')

def newQuotation(request):
    if request.method == 'POST':
        quotationInfo = json.load(request)
        productsData = quotationInfo.get('productsData')
        servicesData = quotationInfo.get('servicesData')
        clientData = quotationInfo.get('clientData')
        sellerData = quotationInfo.get('sellerData')
        quotationData = quotationInfo.get('quotationData')
        documentOptions = quotationInfo.get('documentOptions')
        newQuotationItem = quotationSystem.objects.create(
            endpointQuotation=request.user.extendeduser.endpointUser,
            showDiscount = documentOptions.get('showDiscount'),
            showUnitPrice = documentOptions.get('showUnitPrice'),
            showSellPrice = documentOptions.get('showSellPrice'),
            relatedDocumentQuotation = quotationData.get('relatedDocumentQuotation'),
            commentQuotation = quotationData.get('commentQuotation'),
            quotesQuotation = quotationData.get('quotesQuotation'),
            expirationCredit = quotationData.get('expirationCredit'),
            expirationQuotation = quotationData.get('expirationQuotation'),
            erBuy = quotationData.get('erBuy'),
            erSel = quotationData.get('erSel'),
            stateQuotation = 'GENERADA',
            paymentQuotation = quotationData.get('paymentQuotation'),
            dateQuotation = parse(quotationData.get('dateQuotation')),
            typeQuotation = quotationData.get('typeItems'),
            currencyQuotation = quotationData.get('currencyQuotation'),
        )

        endpointData = endpointSystem.objects.get(id=request.user.extendeduser.endpointUser.id)
        numberQuotation = endpointData.nroCoti
        serieQuotation = endpointData.serieCoti
        newQuotationItem.numberQuotation = numberQuotation
        endpointData.nroCoti = str(int(numberQuotation) + 1)
        endpointData.save()
        newQuotationItem.save()
        codeQuotation = numberQuotation
        while len(codeQuotation) < 4:
            codeQuotation = '0' + codeQuotation
        codeQuotation = f'{serieQuotation}-{codeQuotation}'
        newQuotationItem.codeQuotation = codeQuotation
        newQuotationItem.save()

        clientQuotation = clientSystem.objects.get(id=clientData.get('idClient'))
        idClient=clientData.get('idClient')
        identificationClient=clientData.get('identificationClient')
        documentClient=clientData.get('documentClient')
        typeClient=clientData.get('typeClient')
        emailClient=clientData.get('emailClient')
        contactClient=clientData.get('contactClient')
        phoneClient=clientData.get('phoneClient')
        legalAddressClient=clientData.get('legalAddressClient')
        deliveryAddressClient=clientData.get('deliveryAddress')
        print(deliveryAddressClient)
        dataClientQuotation = [
            idClient,
            identificationClient,
            documentClient,
            typeClient,
            emailClient,
            contactClient,
            phoneClient,
            legalAddressClient,
            deliveryAddressClient,
        ]
        print(dataClientQuotation)
        quotationClientInfo = quotationClientData.objects.create(
            asociatedQuotation=newQuotationItem,
            asociatedClient=clientQuotation,
            dataClientQuotation=dataClientQuotation,
        )
        quotationClientInfo.save()

        sellerQuotation = extendedUser.objects.get(id=sellerData.get('idSeller')).asociatedUser
        idSeller=sellerData.get('idSeller')
        nameSeller=sellerData.get('nameSeller')
        codeSeller=sellerData.get('codeSeller')
        phoneSeller=sellerData.get('phoneSeller')
        dataUserQuotation = [
            idSeller,
            nameSeller,
            codeSeller,
            phoneSeller,
        ]
        quotationSellerInfo = quotationSellerData.objects.create(
            asociatedQuotation=newQuotationItem,
            asociatedUser=sellerQuotation,
            dataUserQuotation=dataUserQuotation,
        )
        quotationSellerInfo.save()

        for productInfo in productsData:
            asociatedProduct = productSystem.objects.get(id=productInfo[0])
            productInfo.append(asociatedProduct.weightProduct)
            quotationProductData.objects.create(
                asociatedQuotation=newQuotationItem,
                asociatedProduct=asociatedProduct,
                dataProductQuotation=productInfo,
            )

        for serviceInfo in servicesData:
            quotationServiceData.objects.create(
                asociatedQuotation=newQuotationItem,
                asociatedService=serviceSystem.objects.get(id=serviceInfo[0]),
                dataServiceQuotation=serviceInfo,
            )
        return JsonResponse({
            'metalprotec':'200',
        })
    return render(request,'newQuotation.html',{
        'clientsSystem':clientSystem.objects.filter(endpointClient=request.user.extendeduser.endpointUser).order_by('id'),
        'usersSystem':extendedUser.objects.filter(endpointUser=request.user.extendeduser.endpointUser).order_by('id'),
        'productsSystem':productSystem.objects.filter(endpointProduct=request.user.extendeduser.endpointUser).order_by('id'),
        'servicesSystem':serviceSystem.objects.filter(endpointService=request.user.extendeduser.endpointUser).order_by('id')
    })

def createGuideFromQuotation(request, idQuotation):
    quotationObject = quotationSystem.objects.get(id=idQuotation)
    quotationObject.stateQuotation = 'EMITIDA'
    quotationObject.save()
    dateGuide = datetime.datetime.today()
    dateGivenGoods = datetime.datetime.today()
    endpointData = endpointSystem.objects.get(id=request.user.extendeduser.endpointUser.id)
    nroGuide = endpointData.nroGuia
    serieGuide = endpointData.serieGuia
    endpointData.nroGuia = str(int(nroGuide) + 1)
    endpointData.save()
    codeGuide = nroGuide
    while len(codeGuide) < 4:
        codeGuide = '0' + codeGuide
    codeGuide = f'{serieGuide}-{codeGuide}'
    guideSystem.objects.create(
        asociatedQuotation=quotationObject,
        dateGuide=dateGuide,
        dateGivenGoods=dateGivenGoods,
        codeGuide=codeGuide,
        nroGuide=nroGuide,
        stateGuide='GENERADA',
        endpointGuide=endpointData
    )
    return HttpResponseRedirect(reverse('salesMetalprotec:guidesMetalprotec'))

def editDataGuide(request,idGuide):
    guideObject = guideSystem.objects.get(id=idGuide)
    return render(request,'editGuide.html',{
        'editGuide':guideObject,
    })

def updateGuide(request):
    if request.method == 'POST':
        guideInfo = json.load(request)
        idGuideInfo = guideInfo.get('idGuideInfo')
        legalAddressClient = guideInfo.get('legalAddressClient')
        deliveryAddress = guideInfo.get('deliveryAddress')
        updatedWeights = guideInfo.get('updatedWeights')
        driverData = guideInfo.get('driverData')
        transporterData = guideInfo.get('transporterData')
        guideData = guideInfo.get('guideData')
        departureData = guideInfo.get('departureData')
        guideObject = guideSystem.objects.get(id=idGuideInfo)
        clientInfoData = guideObject.asociatedQuotation.quotationclientdata
        clientInfoData.dataClientQuotation[7] = legalAddressClient
        clientInfoData.dataClientQuotation[8] = deliveryAddress
        clientInfoData.save()
        guideObject.commentGuide = guideData.get('commentGuide')
        guideObject.dateGuide = parse(guideData.get('dateGuide'))
        guideObject.dateGivenGoods = parse(guideData.get('dateGivenGoods'))
        guideObject.purposeTransportation = guideData.get('purposeTransportation')
        guideObject.modeTransportation = guideData.get('modeTransportation')
        guideObject.extraWeight = guideData.get('extraWeight')
        guideObject.ubigeoClient = guideData.get('ubigeoClient')
        guideObject.deparmentDeparture = departureData.get('deparmentDeparture')
        guideObject.provinceDeparture = departureData.get('provinceDeparture')
        guideObject.districtDeparture = departureData.get('districtDeparture')
        guideObject.addressDeparture = departureData.get('addressDeparture')
        guideObject.ubigeoDeparture = departureData.get('ubigeoDeparture')
        guideObject.razonSocialTranporter = transporterData.get('razonSocialTranporter')
        guideObject.rucTransporter = transporterData.get('rucTransporter')
        guideObject.vehiclePlate = driverData.get('vehiclePlate')
        guideObject.dniDriver = driverData.get('dniDriver')
        guideObject.licenceDriver = driverData.get('licenceDriver')
        guideObject.nameDriver = driverData.get('nameDriver')
        guideObject.save()
        for weightInfo in updatedWeights:
            productObject = quotationProductData.objects.get(id=weightInfo[0])
            productObject.dataProductQuotation[10] = weightInfo[1]
            productObject.save()
        return JsonResponse({
            'metalprotec':'200',
        })

def updateBill(request):
    return JsonResponse({
        'metalprotec':'200',
    })

def updateInvoice(request):
    return JsonResponse({
        'metalprotec':'200',
    })

def createBillFromGuide(request,idGuide):
    guideObject = guideSystem.objects.get(id=idGuide)
    dateBill = datetime.datetime.today()
    endpointData = endpointSystem.objects.get(id=request.user.extendeduser.endpointUser.id)
    numberBill = endpointData.nroFactura
    serieBill = endpointData.serieFactura
    endpointData.nroFactura = str(int(numberBill) + 1)
    endpointData.save()
    codeBill = numberBill
    while len(codeBill) < 4:
        codeBill = '0' + codeBill
    codeBill = f'{serieBill}-{codeBill}'
    dateQuotesBill = []
    if guideObject.asociatedQuotation.paymentQuotation == 'CONTADO':
        dateQuotesBill = []
    else:
        for numberData in range(int(guideObject.asociatedQuotation.numberQuotation)):
            dateQuotesBill.append('2023-01-01')
    billInfo = billSystem.objects.create(
        stateBill='GENERADA',
        dateBill=dateBill,
        erBuy=guideObject.asociatedQuotation.erBuy,
        erSel=guideObject.asociatedQuotation.erSel,
        currencyBill=guideObject.asociatedQuotation.currencyQuotation,
        nroBill = numberBill,
        codeBill = codeBill,
        dateQuotesBill = dateQuotesBill,
        endpointBill=request.user.extendeduser.endpointUser,
    )
    guideObject.asociatedBill = billInfo
    guideObject.save()
    return HttpResponseRedirect(reverse('salesMetalprotec:billsMetalprotec'))


def editDataBill(request,idBill):
    billObject = billSystem.objects.get(id=idBill)
    return render(request,'editBill.html',{
        'editBill':billObject,
    })
