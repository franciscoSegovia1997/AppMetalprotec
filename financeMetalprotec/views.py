from django.shortcuts import render
from . models import bankSystem, paymentSystem, bankOperation, settingsComission
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from salesMetalprotec.models import billSystem, quotationClientData, quotationSystem, invoiceSystem, guideSystem
from clientsMetalprotec.models import clientSystem
import datetime
from django.contrib.auth.models import User
from decimal import Decimal, DecimalException,getcontext
import pandas as pd
import openpyxl

getcontext().prec = 10

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
    return render(request,'comissions.html',{
        'allUsers':User.objects.all().order_by('id').filter(extendeduser__endpointUser=request.user.extendeduser.endpointUser),
    })

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
        guideInfo = request.POST.get('guideInfo')
        quotationInfo = request.POST.get('quotationInfo')
        sellerInfo = request.POST.get('sellerInfo')
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
            codeGuide = guideInfo,
            codeQuotation = quotationInfo,
            codeSeller = sellerInfo,
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
        'allPayments':paymentSystem.objects.filter(endpointPayment=request.user.extendeduser.endpointUser).order_by('-datePayment')
    })

def getDocuments(request):
    finalDocuments = []
    selectedClient = request.GET.get('selectedClient')
    clientInfo = clientSystem.objects.get(id=selectedClient)

    allInvoicesNoGuide = invoiceSystem.objects.exclude(asociatedQuotation=None).exclude(paidInvoice='1').filter(asociatedQuotation__quotationclientdata__asociatedClient=clientInfo)
    allBillsNoGuide = billSystem.objects.exclude(asociatedQuotation=None).exclude(paidBill='1').filter(asociatedQuotation__quotationclientdata__asociatedClient=clientInfo)

    allGuidesBills = guideSystem.objects.filter(asociatedQuotation__quotationclientdata__asociatedClient=clientInfo).filter(asociatedInvoice=None).exclude(asociatedBill=None).exclude(asociatedBill__paidBill='1')
    allGuidesInvoices = guideSystem.objects.filter(asociatedQuotation__quotationclientdata__asociatedClient=clientInfo).filter(asociatedBill=None).exclude(asociatedInvoice=None).exclude(asociatedInvoice__paidInvoice='1')

    for invoiceData in allInvoicesNoGuide:
        if invoiceData.codeInvoice not in finalDocuments:
            finalDocuments.append(invoiceData.codeInvoice)

    for billData in allBillsNoGuide:
        if billData.codeBill not in finalDocuments:
            finalDocuments.append(billData.codeBill)
    
    for guideInfoBill in allGuidesBills:
        if guideInfoBill.asociatedBill.codeBill not in finalDocuments:
            finalDocuments.append(guideInfoBill.asociatedBill.codeBill)
    
    for gudieInfoInvoice in allGuidesInvoices:
        if gudieInfoInvoice.asociatedInvoice.codeInvoice not in finalDocuments:
            finalDocuments.append(gudieInfoInvoice.asociatedInvoice.codeInvoice)

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

def updatePayment(request):
    if request.method == 'POST':
        idPayment = request.POST.get('idPayment')
        paymentObject = paymentSystem.objects.get(id=idPayment)
        idBank = request.POST.get('editBank')
        bankObject = bankSystem.objects.get(id=idBank)
        operationNumber = request.POST.get('editNumber')
        operationNumber2 = request.POST.get('editNumber2')
        datePayment = request.POST.get('editDate')
        paymentObject.asociatedBank = bankObject
        paymentObject.operationNumber = operationNumber
        paymentObject.operationNumber2 = operationNumber2
        paymentObject.datePayment = datetime.datetime.strptime(datePayment,"%Y-%m-%d")
        paymentObject.save()
        statePayment = request.POST.get('editPaid')
        if statePayment == 'on':
            statePayment = 'CANCELADO'
            totalRegisters = paymentSystem.objects.filter(codeDocument=paymentObject.codeDocument)
            for paymentInfo in totalRegisters:
                paymentInfo.statePayment = 'CANCELADO'
                paymentInfo.save()
            if paymentObject.asociatedBill is None:
                asociatedInvoice = paymentObject.asociatedInvoice
                asociatedInvoice.paidInvoice = '1'
                asociatedInvoice.save()
            else:
                asociatedBill = paymentObject.asociatedBill
                asociatedBill.paidBill = '1'
                asociatedBill.save()
        else:
            statePayment = 'PARCIAL'
            totalRegisters = paymentSystem.objects.filter(codeDocument=paymentObject.codeDocument)
            for paymentInfo in totalRegisters:
                paymentInfo.statePayment = 'PARCIAL'
                paymentInfo.save()
            if paymentObject.asociatedBill is None:
                asociatedInvoice = paymentObject.asociatedInvoice
                asociatedInvoice.paidInvoice = '0'
                asociatedInvoice.save()
            else:
                asociatedBill = paymentObject.asociatedBill
                asociatedBill.paidBill = '0'
                asociatedBill.save()
        paymentObject.statePayment = statePayment
        enabledComission = request.POST.get('editComission')
        if enabledComission == 'on':
            enabledComission = 'ON'
            totalRegisters = paymentSystem.objects.filter(codeDocument=paymentObject.codeDocument)
            for paymentInfo in totalRegisters:
                paymentInfo.enabledComission = 'ON'
                paymentInfo.save()
        else:
            enabledComission = 'OFF'
            totalRegisters = paymentSystem.objects.filter(codeDocument=paymentObject.codeDocument)
            for paymentInfo in totalRegisters:
                paymentInfo.enabledComission = 'OFF'
                paymentInfo.save()
        paymentObject.enabledComission = enabledComission
        paymentObject.save()
        return HttpResponseRedirect(reverse('financeMetalprotec:paymentsRegister'))

def getPaymentData(request):
    idPayment = request.GET.get('idPayment')
    paymentInfo = paymentSystem.objects.get(id=idPayment)
    return JsonResponse({
        'editDate':paymentInfo.datePayment.strftime('%Y-%m-%d'),
        'editDocument':paymentInfo.codeDocument,
        'editComission':paymentInfo.enabledComission,
        'editPaid':paymentInfo.statePayment,
        'editClient':paymentInfo.nameClient,
        'editNumber2':paymentInfo.operationNumber2,
        'editNumber':paymentInfo.operationNumber,
        'idBank':str(paymentInfo.asociatedBank.id),
        'guideInfo':paymentInfo.codeGuide,
        'quotationInfo':paymentInfo.codeQuotation,
        'sellerInfo':paymentInfo.codeSeller
    })

def getRelatedDocuments(request):
    guideCode = ''
    quotationCode = ''
    userCode = ''
    documentCode = request.GET.get('documentCode')
    if documentCode[0] == 'F':
        documentObject = billSystem.objects.get(codeBill=documentCode)
    else:
        documentObject = invoiceSystem.objects.get(codeInvoice=documentCode)
    if len(documentObject.guidesystem_set.all()) > 0:
        guideObject = documentObject.guidesystem_set.all()[0]
        guideCode = guideObject.codeGuide
        if guideObject.asociatedQuotation is not None:
            quotationCode = guideObject.asociatedQuotation.codeQuotation
            if guideObject.asociatedQuotation.quotationsellerdata is not None:
                userCode = guideObject.asociatedQuotation.quotationsellerdata.dataUserQuotation[2]
            else:
                userCode = ''
        else:
            quotationCode = ''
            userCode = ''
    else:
        if documentObject.asociatedQuotation is not None:
            guideCode = ''
            quotationCode = documentObject.asociatedQuotation.codeQuotation
            if documentObject.asociatedQuotation.quotationsellerdata is not None:
                userCode = documentObject.asociatedQuotation.quotationsellerdata.dataUserQuotation[2]
            else:
                userCode = ''
        else:
            guideCode = ''
            quotationCode = ''
            userCode = ''
    return JsonResponse({
        'guideCode':guideCode,
        'quotationCode':quotationCode,
        'userCode':userCode
    })

def settingsComissions(request):
    if request.method == 'POST':
        if 'newPartialComission' in request.POST:
            selectedUserComission = request.POST.get('selectedUserComission')
            asociatedUser = User.objects.get(id=selectedUserComission)
            percentageComission = request.POST.get('percentageComission')
            igvIncluded = request.POST.get('igvIncluded')
            if igvIncluded == 'on':
                igvIncluded = 'ON'
            else:
                igvIncluded = 'OFF'
            objComission = settingsComission.objects.create(
                asociatedUserComission=asociatedUser,
                dateRegistered=datetime.datetime.today(),
                igvIncluded=igvIncluded,
                percentageComision=percentageComission,
                typeComission='PARCIAL',
                endpointComission=request.user.extendeduser.endpointUser
            )
            comissionCode = str(objComission.id)
            while len(comissionCode) < 4:
                comissionCode = '0' + comissionCode
            comissionCode = 'COM-' + comissionCode
            objComission.comissionCode = comissionCode
            objComission.save()
            return HttpResponseRedirect(reverse('financeMetalprotec:settingsComissions'))
        if 'newGlobalComission' in request.POST:
            idMainUser = request.POST.get('mainUser')
            asociatedUserComission = User.objects.get(id=idMainUser)
            typeComission = 'GLOBAL'
            endpointComission = request.user.extendeduser.endpointUser
            dateRegistered = datetime.datetime.today()
            idAsociatedUserInfo = request.POST.getlist('idAsociatedUserInfo')
            globalPercentageInfo = request.POST.getlist('globalPercentageInfo')
            globalIgvIncludedInfo = request.POST.getlist('globalIgvIncludedInfo')
            asociatedUsers = []
            for elemento1, elemento2, elemento3 in zip(idAsociatedUserInfo,globalPercentageInfo,globalIgvIncludedInfo):
                asociatedUsers.append([elemento1,elemento2,elemento3])
            objComission = settingsComission.objects.create(
                asociatedUserComission=asociatedUserComission,
                dateRegistered=dateRegistered,
                typeComission=typeComission,
                endpointComission=endpointComission,
                asociatedUsers=asociatedUsers,
            )
            comissionCode = str(objComission.id)
            while len(comissionCode) < 4:
                comissionCode = '0' + comissionCode
            comissionCode = 'COM-' + comissionCode
            objComission.comissionCode = comissionCode
            objComission.save()
            return HttpResponseRedirect(reverse('financeMetalprotec:settingsComissions'))
    return render(request,'settingsComissions.html',{
        'allComissions':settingsComission.objects.all().order_by('-dateRegistered'),
        'allUsers':User.objects.all().order_by('id').filter(extendeduser__endpointUser=request.user.extendeduser.endpointUser),
    })

def deleteSettingComssion(request,idComission):
    selectedComssion = settingsComission.objects.get(id=idComission)
    selectedComssion.delete()
    return HttpResponseRedirect(reverse('financeMetalprotec:settingsComissions'))

def getConfigComission(request):
    userComission = request.GET.get('userComission')
    selectedUser = User.objects.get(id=userComission)
    allConfigComission = settingsComission.objects.filter(asociatedUserComission=selectedUser)
    allConfig = []
    for comissionInfo in allConfigComission:
        allConfig.append([comissionInfo.id,comissionInfo.comissionCode])
    return JsonResponse({
        'allConfig':allConfig,
    })

def getComissionData(request):
    idUserComission = request.GET.get('idUserComission')
    configComission = request.GET.get('configComission')
    monthComission = request.GET.get('monthComission')
    yearComission = request.GET.get('yearComission')
    configObject = settingsComission.objects.get(id=configComission)
    userObject = User.objects.get(id=idUserComission)
    finalValue = Decimal(0.000)
    finalComission = Decimal(0.000)
    comissionData = []
    codeUserInfo = userObject.extendeduser.codeUser
    if configObject.typeComission == 'PARCIAL':
        allPayments = paymentSystem.objects.filter(enabledComission='ON').filter(datePayment__year=int(yearComission)).filter(datePayment__month=int(monthComission)).filter(statePayment='CANCELADO').filter(codeSeller=userObject.extendeduser.codeUser)
        billsPayments = allPayments.filter(asociatedInvoice=None).exclude(asociatedBill=None).order_by('-datePayment')
        invoicesPayments = allPayments.filter(asociatedBill=None).exclude(asociatedInvoice=None).order_by('-datePayment')
        for billInfo in billsPayments:
            comissionData.append([
                billInfo.datePayment.strftime('%d-%m-%Y'),
                billInfo.nameBankPayment,
                billInfo.nameClient,
                billInfo.codeDocument,
                billInfo.codeQuotation,
                billInfo.operationNumber,
                billInfo.operationNumber2
            ])
        for invoiceInfo in invoicesPayments:
            comissionData.append([
                invoiceInfo.datePayment.strftime('%d-%m-%Y'),
                invoiceInfo.nameBankPayment,
                invoiceInfo.nameClient,
                invoiceInfo.codeDocument,
                invoiceInfo.codeQuotation,
                invoiceInfo.operationNumber,
                invoiceInfo.operationNumber2
            ])

        billsCodes = []
        invoicesCodes = []
        for billInfo in billsPayments:
            if billInfo.codeDocument not in billsCodes:
                billsCodes.append(billInfo.codeDocument)
        for invoiceInfo in invoicesPayments:
            if invoiceInfo.codeDocument not in invoicesCodes:
                invoicesCodes.append(invoiceInfo.codeDocument)
        #Calculo de las comisiones y venta total
        totalValue = Decimal(0.000)
        comissionValue = Decimal(0.000)
        for codeInfo in billsCodes:
            billObject = billSystem.objects.get(codeBill=codeInfo)
            if billObject.asociatedQuotation is not None:
                quotationObject = billObject.asociatedQuotation
                totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                for productInfo in totalProductsQuotation:
                    if productInfo.dataProductQuotation[5] == 'DOLARES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[5] == 'SOLES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[9] == '1':
                        v_producto = Decimal(0.00)
                    totalValue = Decimal(totalValue) + Decimal(v_producto)
            else:
                quotationObject = billObject.guidesystem_set.all()[0].asociatedQuotation
                totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                for productInfo in totalProductsQuotation:
                    if productInfo.dataProductQuotation[5] == 'DOLARES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[5] == 'SOLES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[9] == '1':
                        v_producto = Decimal(0.00)
                    totalValue = Decimal(totalValue) + Decimal(v_producto)

        for codeInfo in invoicesCodes:
            invoiceObject = invoiceSystem.objects.get(codeInvoice=codeInfo)
            if invoiceObject.asociatedQuotation is not None:
                quotationObject = invoiceObject.asociatedQuotation
                totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                for productInfo in totalProductsQuotation:
                    if productInfo.dataProductQuotation[5] == 'DOLARES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(invoiceObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[5] == 'SOLES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[9] == '1':
                        v_producto = Decimal(0.00)
                    totalValue = Decimal(totalValue) + Decimal(v_producto)
            else:
                quotationObject = invoiceObject.guidesystem_set.all()[0].asociatedQuotation
                totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                for productInfo in totalProductsQuotation:
                    if productInfo.dataProductQuotation[5] == 'DOLARES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(invoiceObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[5] == 'SOLES':
                        v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                        v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                    if productInfo.dataProductQuotation[9] == '1':
                        v_producto = Decimal(0.00)
                    totalValue = Decimal(totalValue) + Decimal(v_producto)
        if configObject.igvIncluded == 'ON':
            totalValue = Decimal('%.2f' % totalValue)*Decimal(1.18)
        comisionValue = (totalValue*Decimal(float(configObject.percentageComision)))/Decimal(100)
        comisionValue =  Decimal('%.2f' % comisionValue)
        finalComission = comisionValue
        finalValue = totalValue
    else:
        for configInfo in configObject.asociatedUsers:
            userObject1 = User.objects.get(id=configInfo[0])
            allPayments = paymentSystem.objects.filter(enabledComission='ON').filter(datePayment__year=int(yearComission)).filter(datePayment__month=int(monthComission)).filter(statePayment='CANCELADO').filter(codeSeller=userObject1.extendeduser.codeUser)
            billsPayments = allPayments.filter(asociatedInvoice=None).exclude(asociatedBill=None).order_by('-datePayment')
            invoicesPayments = allPayments.filter(asociatedBill=None).exclude(asociatedInvoice=None).order_by('-datePayment')
            for billInfo in billsPayments:
                comissionData.append([
                    billInfo.datePayment.strftime('%d-%m-%Y'),
                    billInfo.nameBankPayment,
                    billInfo.nameClient,
                    billInfo.codeDocument,
                    billInfo.codeQuotation,
                    billInfo.operationNumber,
                    billInfo.operationNumber2
                ])
            for invoiceInfo in invoicesPayments:
                comissionData.append([
                    invoiceInfo.datePayment.strftime('%d-%m-%Y'),
                    invoiceInfo.nameBankPayment,
                    invoiceInfo.nameClient,
                    invoiceInfo.codeDocument,
                    invoiceInfo.codeQuotation,
                    invoiceInfo.operationNumber,
                    invoiceInfo.operationNumber2
                ])
            
            billsCodes = []
            invoicesCodes = []
            for billInfo in billsPayments:
                if billInfo.codeDocument not in billsCodes:
                    billsCodes.append(billInfo.codeDocument)
            for invoiceInfo in invoicesPayments:
                if invoiceInfo.codeDocument not in invoicesCodes:
                    invoicesCodes.append(invoiceInfo.codeDocument)
            #Calculo de las comisiones y venta total
            totalValue = Decimal(0.000)
            comissionValue = Decimal(0.000)
            for codeInfo in billsCodes:
                billObject = billSystem.objects.get(codeBill=codeInfo)
                if billObject.asociatedQuotation is not None:
                    quotationObject = billObject.asociatedQuotation
                    totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                    for productInfo in totalProductsQuotation:
                        if productInfo.dataProductQuotation[5] == 'DOLARES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[5] == 'SOLES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[9] == '1':
                            v_producto = Decimal(0.00)
                        totalValue = Decimal(totalValue) + Decimal(v_producto)
                else:
                    quotationObject = billObject.guidesystem_set.all()[0].asociatedQuotation
                    totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                    for productInfo in totalProductsQuotation:
                        if productInfo.dataProductQuotation[5] == 'DOLARES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[5] == 'SOLES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[9] == '1':
                            v_producto = Decimal(0.00)
                        totalValue = Decimal(totalValue) + Decimal(v_producto)

            for codeInfo in invoicesCodes:
                invoiceObject = invoiceSystem.objects.get(codeInvoice=codeInfo)
                if invoiceObject.asociatedQuotation is not None:
                    quotationObject = invoiceObject.asociatedQuotation
                    totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                    for productInfo in totalProductsQuotation:
                        if productInfo.dataProductQuotation[5] == 'DOLARES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(invoiceObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[5] == 'SOLES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[9] == '1':
                            v_producto = Decimal(0.00)
                        totalValue = Decimal(totalValue) + Decimal(v_producto)
                else:
                    quotationObject = invoiceObject.guidesystem_set.all()[0].asociatedQuotation
                    totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                    for productInfo in totalProductsQuotation:
                        if productInfo.dataProductQuotation[5] == 'DOLARES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(invoiceObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[5] == 'SOLES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[9] == '1':
                            v_producto = Decimal(0.00)
                        totalValue = Decimal(totalValue) + Decimal(v_producto)

            if configInfo[2] == 'ON':
                totalValue = Decimal('%.2f' % totalValue)*Decimal(1.18)
            comisionValue = (totalValue*Decimal(float(configInfo[1])))/Decimal(100)
            comisionValue =  Decimal('%.2f' % comisionValue)
            finalComission = Decimal(finalComission) + Decimal(comisionValue)
            finalValue = Decimal(finalValue) + Decimal(totalValue)

    finalComission = str(finalComission)
    finalValue = str(finalValue)

                    
    return JsonResponse({
        'comissionData':comissionData,
        'finalValue':finalValue,
        'codeUserInfo':codeUserInfo,
        'finalComission':finalComission
    })

def exportComissions(request):
    if request.method == 'POST':
        idUserComission = request.POST.get('idUserComission')
        configComission = request.POST.get('configComission')
        monthComission = request.POST.get('monthComission')
        yearComission = request.POST.get('yearComission')

        print(idUserComission)
        print(configComission)
        print(monthComission)
        print(yearComission)

        configObject = settingsComission.objects.get(id=configComission)
        userObject = User.objects.get(id=idUserComission)
        finalValue = Decimal(0.000)
        finalComission = Decimal(0.000)
        comissionData = []
        codeUserInfo = userObject.extendeduser.codeUser
        if configObject.typeComission == 'PARCIAL':
            allPayments = paymentSystem.objects.filter(enabledComission='ON').filter(datePayment__year=int(yearComission)).filter(datePayment__month=int(monthComission)).filter(statePayment='CANCELADO').filter(codeSeller=userObject.extendeduser.codeUser)
            billsPayments = allPayments.filter(asociatedInvoice=None).exclude(asociatedBill=None).order_by('-datePayment')
            invoicesPayments = allPayments.filter(asociatedBill=None).exclude(asociatedInvoice=None).order_by('-datePayment')
            for billInfo in billsPayments:
                comissionData.append([
                    billInfo.datePayment.strftime('%d-%m-%Y'),
                    billInfo.nameBankPayment,
                    billInfo.nameClient,
                    billInfo.codeDocument,
                    billInfo.codeQuotation,
                    billInfo.operationNumber,
                    billInfo.operationNumber2,
                    billInfo.currencyBill
                ])
            for invoiceInfo in invoicesPayments:
                comissionData.append([
                    invoiceInfo.datePayment.strftime('%d-%m-%Y'),
                    invoiceInfo.nameBankPayment,
                    invoiceInfo.nameClient,
                    invoiceInfo.codeDocument,
                    invoiceInfo.codeQuotation,
                    invoiceInfo.operationNumber,
                    invoiceInfo.operationNumber2,
                    invoiceInfo.currencyInvoice
                ])

            billsCodes = []
            invoicesCodes = []
            for billInfo in billsPayments:
                if billInfo.codeDocument not in billsCodes:
                    billsCodes.append(billInfo.codeDocument)
            for invoiceInfo in invoicesPayments:
                if invoiceInfo.codeDocument not in invoicesCodes:
                    invoicesCodes.append(invoiceInfo.codeDocument)
            #Calculo de las comisiones y venta total
            totalValue = Decimal(0.000)
            comissionValue = Decimal(0.000)
            for codeInfo in billsCodes:
                billObject = billSystem.objects.get(codeBill=codeInfo)
                if billObject.asociatedQuotation is not None:
                    quotationObject = billObject.asociatedQuotation
                    totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                    for productInfo in totalProductsQuotation:
                        if productInfo.dataProductQuotation[5] == 'DOLARES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[5] == 'SOLES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[9] == '1':
                            v_producto = Decimal(0.00)
                        totalValue = Decimal(totalValue) + Decimal(v_producto)
                else:
                    quotationObject = billObject.guidesystem_set.all()[0].asociatedQuotation
                    totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                    for productInfo in totalProductsQuotation:
                        if productInfo.dataProductQuotation[5] == 'DOLARES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[5] == 'SOLES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[9] == '1':
                            v_producto = Decimal(0.00)
                        totalValue = Decimal(totalValue) + Decimal(v_producto)

            for codeInfo in invoicesCodes:
                invoiceObject = invoiceSystem.objects.get(codeInvoice=codeInfo)
                if invoiceObject.asociatedQuotation is not None:
                    quotationObject = invoiceObject.asociatedQuotation
                    totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                    for productInfo in totalProductsQuotation:
                        if productInfo.dataProductQuotation[5] == 'DOLARES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(invoiceObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[5] == 'SOLES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[9] == '1':
                            v_producto = Decimal(0.00)
                        totalValue = Decimal(totalValue) + Decimal(v_producto)
                else:
                    quotationObject = invoiceObject.guidesystem_set.all()[0].asociatedQuotation
                    totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                    for productInfo in totalProductsQuotation:
                        if productInfo.dataProductQuotation[5] == 'DOLARES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(invoiceObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[5] == 'SOLES':
                            v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                            v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                        if productInfo.dataProductQuotation[9] == '1':
                            v_producto = Decimal(0.00)
                        totalValue = Decimal(totalValue) + Decimal(v_producto)
            if configObject.igvIncluded == 'ON':
                totalValue = Decimal('%.2f' % totalValue)*Decimal(1.18)
            comisionValue = (totalValue*Decimal(float(configObject.percentageComision)))/Decimal(100)
            comisionValue =  Decimal('%.2f' % comisionValue)
            finalComission = comisionValue
            finalValue = totalValue
        else:
            for configInfo in configObject.asociatedUsers:
                userObject1 = User.objects.get(id=configInfo[0])
                allPayments = paymentSystem.objects.filter(enabledComission='ON').filter(datePayment__year=int(yearComission)).filter(datePayment__month=int(monthComission)).filter(statePayment='CANCELADO').filter(codeSeller=userObject1.extendeduser.codeUser)
                billsPayments = allPayments.filter(asociatedInvoice=None).exclude(asociatedBill=None).order_by('-datePayment')
                invoicesPayments = allPayments.filter(asociatedBill=None).exclude(asociatedInvoice=None).order_by('-datePayment')
                for billInfo in billsPayments:
                    comissionData.append([
                        billInfo.datePayment.strftime('%d-%m-%Y'),
                        billInfo.nameBankPayment,
                        billInfo.nameClient,
                        billInfo.codeDocument,
                        billInfo.codeQuotation,
                        billInfo.operationNumber,
                        billInfo.operationNumber2,
                        billInfo.currencyBill
                    ])
                for invoiceInfo in invoicesPayments:
                    comissionData.append([
                        invoiceInfo.datePayment.strftime('%d-%m-%Y'),
                        invoiceInfo.nameBankPayment,
                        invoiceInfo.nameClient,
                        invoiceInfo.codeDocument,
                        invoiceInfo.codeQuotation,
                        invoiceInfo.operationNumber,
                        invoiceInfo.operationNumber2,
                        invoiceInfo.currencyInvoice
                    ])
                
                billsCodes = []
                invoicesCodes = []
                for billInfo in billsPayments:
                    if billInfo.codeDocument not in billsCodes:
                        billsCodes.append(billInfo.codeDocument)
                for invoiceInfo in invoicesPayments:
                    if invoiceInfo.codeDocument not in invoicesCodes:
                        invoicesCodes.append(invoiceInfo.codeDocument)
                #Calculo de las comisiones y venta total
                totalValue = Decimal(0.000)
                comissionValue = Decimal(0.000)
                for codeInfo in billsCodes:
                    billObject = billSystem.objects.get(codeBill=codeInfo)
                    if billObject.asociatedQuotation is not None:
                        quotationObject = billObject.asociatedQuotation
                        totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                        for productInfo in totalProductsQuotation:
                            if productInfo.dataProductQuotation[5] == 'DOLARES':
                                v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                                v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                            if productInfo.dataProductQuotation[5] == 'SOLES':
                                v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                                v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                            if productInfo.dataProductQuotation[9] == '1':
                                v_producto = Decimal(0.00)
                            totalValue = Decimal(totalValue) + Decimal(v_producto)
                    else:
                        quotationObject = billObject.guidesystem_set.all()[0].asociatedQuotation
                        totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                        for productInfo in totalProductsQuotation:
                            if productInfo.dataProductQuotation[5] == 'DOLARES':
                                v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(quotationObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                                v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                            if productInfo.dataProductQuotation[5] == 'SOLES':
                                v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                                v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                            if productInfo.dataProductQuotation[9] == '1':
                                v_producto = Decimal(0.00)
                            totalValue = Decimal(totalValue) + Decimal(v_producto)

                for codeInfo in invoicesCodes:
                    invoiceObject = invoiceSystem.objects.get(codeInvoice=codeInfo)
                    if invoiceObject.asociatedQuotation is not None:
                        quotationObject = invoiceObject.asociatedQuotation
                        totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                        for productInfo in totalProductsQuotation:
                            if productInfo.dataProductQuotation[5] == 'DOLARES':
                                v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(invoiceObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                                v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                            if productInfo.dataProductQuotation[5] == 'SOLES':
                                v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                                v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                            if productInfo.dataProductQuotation[9] == '1':
                                v_producto = Decimal(0.00)
                            totalValue = Decimal(totalValue) + Decimal(v_producto)
                    else:
                        quotationObject = invoiceObject.guidesystem_set.all()[0].asociatedQuotation
                        totalProductsQuotation = quotationObject.quotationproductdata_set.all()
                        for productInfo in totalProductsQuotation:
                            if productInfo.dataProductQuotation[5] == 'DOLARES':
                                v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(invoiceObject.erSel)*Decimal(Decimal(1.00) - Decimal(productInfo.dataProductQuotation[7])/100)
                                v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                            if productInfo.dataProductQuotation[5] == 'SOLES':
                                v_producto = Decimal(productInfo.dataProductQuotation[6])*Decimal(Decimal(1.00) - (Decimal(productInfo.dataProductQuotation[7])/100))
                                v_producto = Decimal('%.2f' % v_producto)*Decimal(productInfo.dataProductQuotation[8])
                            if productInfo.dataProductQuotation[9] == '1':
                                v_producto = Decimal(0.00)
                            totalValue = Decimal(totalValue) + Decimal(v_producto)

                if configInfo[2] == 'ON':
                    totalValue = Decimal('%.2f' % totalValue)*Decimal(1.18)
                comisionValue = (totalValue*Decimal(float(configInfo[1])))/Decimal(100)
                comisionValue =  Decimal('%.2f' % comisionValue)
                finalComission = Decimal(finalComission) + Decimal(comisionValue)
                finalValue = Decimal(finalValue) + Decimal(totalValue)

        finalComission = str(finalComission)
        finalValue = str(finalValue)

        comissionData.append(['','','','','','','MONTO TOTAL: ',f"{finalValue}"])
        comissionData.append(['','','','','','','MONTO COMISION: ',f"{finalComission}"])

        tabla_excel = pd.DataFrame(comissionData,columns=['Fecha','Banco','Cliente','Comprobante','Cotizacion','Nro Operarion','Nro Operacion 2','Moneda'])
        tabla_excel.to_excel('comissionsInfo.xlsx',index=False)
        doc_excel = openpyxl.load_workbook("comissionsInfo.xlsx")
        doc_excel.active.column_dimensions['A'].width = 20
        doc_excel.active.column_dimensions['B'].width = 20
        doc_excel.active.column_dimensions['C'].width = 60
        doc_excel.active.column_dimensions['D'].width = 20
        doc_excel.active.column_dimensions['E'].width = 20
        doc_excel.active.column_dimensions['F'].width = 30
        doc_excel.active.column_dimensions['G'].width = 30
        doc_excel.active.column_dimensions['H'].width = 25
        doc_excel.save("comissionsInfo.xlsx")


        response = HttpResponse(open('comissionsInfo.xlsx','rb'),content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        nombre = 'attachment; ' + 'filename=' + 'comissionsInfo.xlsx'
        response['Content-Disposition'] = nombre
        return response