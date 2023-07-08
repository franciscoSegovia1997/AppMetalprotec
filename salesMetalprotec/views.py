from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from clientsMetalprotec.models import clientSystem
from productsMetalprotec.models import productSystem
from django.contrib.auth.models import User
from servicesMetalprotec.models import serviceSystem
from usersMetalprotec.models import extendedUser
from settingsMetalprotec.models import endpointSystem
from .models import quotationSystem, quotationClientData, quotationProductData, quotationSellerData, quotationServiceData
from dateutil.parser import parse
import json

# Create your views here.
def quotationsMetalprotec(request):
    return render(request,'quotationsMetalprotec.html',{
        'quotationsSystem':quotationSystem.objects.filter(endpointQuotation=request.user.extendeduser.endpointUser).order_by('id')
    })

def guidesMetalprotec(request):
    return render(request,'guidesMetalprotec.html')

def billsMetalprotec(request):
    return render(request,'billsMetalprotec.html')

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
        deliveryAddressClient=clientData.get('deliveryAddressClient')
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
            quotationProductData.objects.create(
                asociatedQuotation=newQuotationItem,
                asociatedProduct=productSystem.objects.get(id=productInfo[0]),
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