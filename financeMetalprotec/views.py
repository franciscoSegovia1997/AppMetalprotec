from django.shortcuts import render
from . models import bankSystem, paymentSystem, bankOperation, settingsComission
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from salesMetalprotec.models import billSystem
from clientsMetalprotec.models import clientSystem
import datetime

# Create your views here.
def bankRegisters(request):
    if request.method == 'POST':
        nameBank = request.POST.get('nameBank')
        currencyBank = request.POST.get('currencyBank')
        accountNumber = request.POST.get('accountNumber')
        moneyBank = request.POST.get('moneyBank')
        bankSystem.objects.create(
            nameBank=nameBank,
            currencyBank=currencyBank,
            accountNumber=accountNumber,
            moneyBank=moneyBank,
            endpointBank=request.user.extendeduser.endpointUser,
        )
    return render(request,'bankRegisters.html',{
        'bankRegistersSystem':bankSystem.objects.filter(endpointBank=request.user.extendeduser.endpointUser)
    })

def comissions(request):
    return render(request,'comissions.html')

def paymentsRegister(request):
    if request.method == 'POST':
        selectedBank = request.POST.get('selectedBank')
        operationNumber = request.POST.get('operationNumber')
        operationNumber2 = request.POST.get('operationNumber2')
        selectedClient = request.POST.get('selectedClient')
        selectedDocument = request.POST.get('selectedDocument')
        datePayment = request.POST.get('datePayment')
        enabledComission = request.POST.get('enabledComission')
        paidDocument = request.POST.get('paidDocument')
        asociatedBank = bankSystem.objects.get(id=selectedBank)
        endpointPayment = request.user.extendeduser.endpointUser
        asociatedClient = clientSystem.objects.get(id=selectedClient)

        if asociatedClient.typeClient == 'PERSONA':
            typeDocumentPayment = 'INVOICE'
            asociatedInvoice = invoiceSystem.objects.get(codeInvoice=selectedDocument)
            asociatedBill = None
        else:
            typeDocumentPayment = 'BILL'
            asociatedBill = billSystem.objects.get(codeBill=selectedDocument)
            asociatedInvoice = None

        if paidDocument == 'on':
            statePayment = 'CANCELADO'
            totalRegisters = paymentSystem.objects.filter(codeDocument=selectedDocument)
            for paymentInfo in totalRegisters:
                paymentInfo.statePayment = 'CANCELADO'
                paymentInfo.save()
            if asociatedBill is None:
                asociatedInvoice.paidInvoice = '1'
                asociatedInvoice.save()
            else:
                asociatedBill.paidBill = '1'
                asociatedBill.save()
        else:
            statePayment = 'PARCIAL'
            totalRegisters = paymentSystem.objects.filter(codeDocument=selectedDocument)
            for paymentInfo in totalRegisters:
                paymentInfo.statePayment = 'PARCIAL'
                paymentInfo.save()
            if asociatedBill is None:
                asociatedInvoice.paidInvoice = '0'
                asociatedInvoice.save()
            else:
                asociatedBill.paidBill = '0'
                asociatedBill.save()

        if enabledComission == 'on':
            enabledComission = 'ON'
            totalRegisters = paymentSystem.objects.filter(codeDocument=selectedDocument)
            for paymentInfo in totalRegisters:
                paymentInfo.enabledComission = 'ON'
                paymentInfo.save()
        else:
            enabledComission = 'OFF'
            totalRegisters = paymentSystem.objects.filter(codeDocument=selectedDocument)
            for paymentInfo in totalRegisters:
                paymentInfo.enabledComission = 'OFF'
                paymentInfo.save()

        paymentSystem.objects.create(
            datePayment = datetime.datetime.strptime(datePayment,'%Y-%m-%d'),
            nameBankPayment = asociatedBank.nameBank,
            currencyPayment = asociatedBank.currencyBank,
            operationNumber = operationNumber,
            operationNumber2 = operationNumber2,
            nameClient = asociatedClient.identificationClient,
            statePayment = statePayment,
            codeDocument = selectedDocument,
            codeGuide = '',
            codeQuotation = '',
            codeSeller = '',
            typeDocumentPayment = typeDocumentPayment,
            enabledComission = enabledComission,
            asociatedBank = asociatedBank,
            asociatedBill = asociatedBill,
            asociatedInvoice = asociatedInvoice,
            endpointPayment = endpointPayment
        )
        return HttpResponseRedirect(reverse('financeMetalprotec:paymentsRegister'))
    return render(request,'paymentsRegister.html',{
        'allBanks':bankSystem.objects.all().order_by('id'),
        'allClients':clientSystem.objects.all().order_by('id'),
        'allPayments':paymentSystem.objects.filter(endpointPayment=request.user.extendeduser.endpointUser)
    })

def getDocuments(request):
    finalDocuments = []
    selectedClient = request.GET.get('selectedClient')
    clientInfo = clientSystem.objects.get(id=selectedClient)
    if clientInfo.typeClient == 'PERSONA':
        allDocuments = invoiceSystem.objects.exclude(paidInvoice='1')
        for documentInfo in allDocuments:
            if documentInfo.originInvoice == 'GUIDE':
                if documentInfo.guidesystem_set.all()[0].asociatedQuotation.quotationclientdata.asociatedClient == clientInfo:
                    finalDocuments.append(documentInfo.codeBill)
            else:
                if documentInfo.asociatedQuotation.quotationclientdata.asociatedClient == clientInfo:
                    finalDocuments.append(documentInfo.codeBill)
    else:
        allDocuments = billSystem.objects.all().exclude(paidBill='1')
        for documentInfo in allDocuments:
            if documentInfo.originBill == 'GUIDE':
                if documentInfo.guidesystem_set.all()[0].asociatedQuotation.quotationclientdata.asociatedClient == clientInfo:
                    finalDocuments.append(documentInfo.codeBill)
            else:
                if documentInfo.asociatedQuotation.quotationclientdata.asociatedClient == clientInfo:
                    finalDocuments.append(documentInfo.codeBill)
    return JsonResponse({
        'finalDocuments':finalDocuments,
    })

def deletePayment(request,idPayment):
    paymentInfo = paymentSystem.objects.get(id=idPayment)
    totalRegisters = paymentSystem.objects.filter(codeDocument=paymentInfo.codeDocument)
    for paymentInfo in totalRegisters:
        paymentInfo.statePayment = 'PARCIAL'
        paymentInfo.save()
    if paymentInfo.asociatedBill is None:
        asociatedInvoice = paymentInfo.asociatedInvoice
        asociatedInvoice.paidInvoice = '0'
        asociatedInvoice.save()
    else:
        asociatedBill = paymentInfo.asociatedBill
        asociatedBill.paidBill = '0'
        asociatedBill.save()
    paymentInfo.delete()
    return HttpResponseRedirect(reverse('financeMetalprotec:paymentsRegister'))


def deleteBankRegister(request,idBank):
    bankSystem.objects.get(id=idBank).delete()
    return HttpResponseRedirect(reverse('financeMetalprotec:bankRegisters'))