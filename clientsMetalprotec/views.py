from django.shortcuts import render
from .models import clientSystem, addressClient
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def clientsMetalprotec(request):
    if request.method == 'POST':
        if 'newClient' in request.POST:
            identificationClient = request.POST.get('identificationClient')
            documentClient = request.POST.get('documentClient')
            emailClient = request.POST.get('emailClient')
            legalAddressClient = request.POST.get('legalAddressClient')
            contactClient = request.POST.get('contactClient')
            phoneClient = request.POST.get('phoneClient')
            typeClient = request.POST.get('typeClient')
            enabledCommission = request.POST.get('enabledCommission')
            if enabledCommission == 'on':
                enabledCommission='ON'
            else:
                enabledCommission='OFF'
            endpointClient = request.user.extendeduser.endpointUser
            clientSystem.objects.create(
                identificationClient=identificationClient,
                documentClient=documentClient,
                emailClient=emailClient,
                legalAddressClient=legalAddressClient,
                contactClient=contactClient,
                phoneClient=phoneClient,
                typeClient=typeClient,
                enabledCommission=enabledCommission,
                endpointClient=endpointClient
            )
            return HttpResponseRedirect(reverse('clientsMetalprotec:clientsMetalprotec'))
    return render(request,'clientsMetalprotec.html',{
        'clientsSystem':clientSystem.objects.filter(endpointClient=request.user.extendeduser.endpointUser).order_by('id')
    })

@login_required(login_url='/')
def deleteClient(request):
    if request.method == 'POST':
        deleteIdClient = request.POST.get('deleteIdClient')
        deleteClient = clientSystem.objects.get(id=deleteIdClient)
        deleteClient.delete()
        return HttpResponseRedirect(reverse('clientsMetalprotec:clientsMetalprotec'))

@login_required(login_url='/')
def getClientData(request):
    idClient=request.GET.get('idClient')
    editClient=clientSystem.objects.get(id=idClient)
    return JsonResponse({
        'editDocumentClient':editClient.documentClient,
        'editIdentificationClient':editClient.identificationClient,
        'editTypeClient':editClient.typeClient,
        'editEmailClient':editClient.emailClient,
        'editContactClient':editClient.contactClient,
        'editPhoneClient':editClient.phoneClient,
        'editLegalAddressClient':editClient.legalAddressClient,
        'editEnabledCommission':editClient.enabledCommission,
    })

@login_required(login_url='/')
def updateClient(request):
    if request.method == 'POST':
        editIdClient=request.POST.get('editIdClient')
        editDocumentClient=request.POST.get('editDocumentClient')
        editIdentificationClient=request.POST.get('editIdentificationClient')
        editTypeClient=request.POST.get('editTypeClient')
        editEmailClient=request.POST.get('editEmailClient')
        editContactClient=request.POST.get('editContactClient')
        editPhoneClient=request.POST.get('editPhoneClient')
        editLegalAddressClient=request.POST.get('editLegalAddressClient')
        editEnabledCommission=request.POST.get('editEnabledCommission')

        if editEnabledCommission == 'on':
            editEnabledCommission='ON'
        else:
            editEnabledCommission='OFF'
        
        editClient = clientSystem.objects.get(id=editIdClient)
        editClient.documentClient=editDocumentClient
        editClient.identificationClient=editIdentificationClient
        editClient.typeClient=editTypeClient
        editClient.emailClient=editEmailClient
        editClient.contactClient=editContactClient
        editClient.phoneClient=editPhoneClient
        editClient.legalAddressClient=editLegalAddressClient
        editClient.enabledCommission=editEnabledCommission
        editClient.save()
        return HttpResponseRedirect(reverse('clientsMetalprotec:clientsMetalprotec'))
    
def getClientAddress(request):
    idClient = request.GET.get('idClient')
    editClient = clientSystem.objects.get(id=idClient)
    addressesClient = []
    for deliveryClient in editClient.addressclient_set.all():
        addressesClient.append(deliveryClient.deliveryAddress)
    return JsonResponse({
        'addressesClient':addressesClient,
    })

def addClientAddress(request):
    if request.method == 'POST':
        idClient = request.POST.get('addAddressClient')
        deliveryAddress = request.POST.get('newClientAddress')
        asociatedClient = clientSystem.objects.get(id=idClient)
        addressClient.objects.create(
            deliveryAddress=deliveryAddress,
            asociatedClient=asociatedClient,
        )
        return HttpResponseRedirect(reverse('clientsMetalprotec:clientsMetalprotec'))
    
def importClientsData(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('clientsMetalprotec:clientsMetalprotec'))