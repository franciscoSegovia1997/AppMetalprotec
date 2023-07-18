from django.db import models
from clientsMetalprotec.models import clientSystem
from settingsMetalprotec.models import endpointSystem
from django.contrib.postgres.fields import ArrayField
from productsMetalprotec.models import productSystem
from servicesMetalprotec.models import serviceSystem
from django.contrib.auth.models import User

# Create your models here.
class quotationSystem(models.Model):
    showDiscount = models.CharField(max_length=4, null=True, blank=True)
    showUnitPrice = models.CharField(max_length=4, null=True, blank=True)
    showSellPrice = models.CharField(max_length=4, null=True, blank=True)
    relatedDocumentQuotation = models.CharField(max_length=24, null=True, blank=True)
    commentQuotation = models.CharField(max_length=256, null=True, blank=True)
    quotesQuotation = models.CharField(max_length=12, null=True, blank=True)
    expirationCredit = models.CharField(max_length=12,null=True,blank=True)
    expirationQuotation = models.CharField(max_length=12,null=True,blank=True)
    numberQuotation = models.CharField(max_length=8, null=True, blank=True)
    erBuy = models.CharField(max_length=8, null=True, blank=True)
    erSel = models.CharField(max_length=8, null=True, blank=True)
    codeQuotation = models.CharField(max_length=16, null=True, blank=True)
    stateQuotation = models.CharField(max_length=12, null=True, blank=True)
    paymentQuotation = models.CharField(max_length=12, null=True, blank=True)
    dateQuotation = models.DateField(null=True,blank=True)
    typeQuotation = models.CharField(max_length=12, null=True, blank=True)
    currencyQuotation = models.CharField(max_length=12,null=True,blank=True)
    endpointQuotation = models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.codeQuotation}'

class quotationClientData(models.Model):
    asociatedQuotation = models.OneToOneField(quotationSystem,on_delete=models.CASCADE, blank=True, null=True)
    asociatedClient = models.ForeignKey(clientSystem, on_delete=models.SET_NULL, null=True, blank=True)
    dataClientQuotation = ArrayField(models.CharField(max_length=256),null=True, blank=True)

class quotationSellerData(models.Model):
    asociatedQuotation = models.OneToOneField(quotationSystem,on_delete=models.CASCADE, blank=True, null=True)
    asociatedUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    dataUserQuotation = ArrayField(models.CharField(max_length=256),null=True, blank=True)

class quotationProductData(models.Model):
    asociatedQuotation = models.ForeignKey(quotationSystem,on_delete=models.CASCADE, blank=True, null=True)
    asociatedProduct = models.ForeignKey(productSystem, on_delete=models.SET_NULL, null=True, blank=True)
    dataProductQuotation = ArrayField(models.CharField(max_length=256),null=True, blank=True)
    weightProduct = models.CharField(max_length=8,blank=True, null=True)

class quotationServiceData(models.Model):
    asociatedQuotation = models.ForeignKey(quotationSystem,on_delete=models.CASCADE, blank=True, null=True)
    asociatedService = models.ForeignKey(serviceSystem, on_delete=models.SET_NULL, null=True, blank=True)
    dataServiceQuotation = ArrayField(models.CharField(max_length=256),null=True,blank=True)

class billSystem(models.Model):
    commentBill = models.CharField(max_length=256, null=True, blank=True)
    dateBill = models.DateField(null=True,blank=True)
    relatedDocumentBill = models.CharField(max_length=24,null=True,blank=True)
    dateQuotesBill = ArrayField(models.CharField(max_length=256),null=True, blank=True)
    erBuy = models.CharField(max_length=8, null=True, blank=True)
    erSel = models.CharField(max_length=8, null=True, blank=True)
    currencyBill = models.CharField(max_length=12,null=True,blank=True)
    stateBill = models.CharField(max_length=12,null=True,blank=True)
    codeBill = models.CharField(max_length=12,null=True,blank=True)
    stateTeFacturo = models.CharField(max_length=24,null=True,blank=True)
    nroBill = models.CharField(max_length=12,null=True,blank=True)
    typeItemsBill = models.CharField(max_length=12,null=True,blank=True)
    originBill = models.CharField(max_length=12,null=True,blank=True)
    asociatedQuotation = models.OneToOneField(quotationSystem,on_delete=models.CASCADE, blank=True, null=True)
    endpointBill = models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

class invoiceSystem(models.Model):
    commentInvoice = models.CharField(max_length=256, null=True, blank=True)
    dateInvoice = models.DateField(null=True,blank=True)
    relatedDocumentInvoice = models.CharField(max_length=24,null=True,blank=True)
    dateQuotesInvoice = ArrayField(models.CharField(max_length=256),null=True, blank=True)
    erBuy = models.CharField(max_length=8, null=True, blank=True)
    erSel = models.CharField(max_length=8, null=True, blank=True)
    currencyInvoice = models.CharField(max_length=12,null=True,blank=True)
    stateInvoice = models.CharField(max_length=12,null=True,blank=True)
    codeInvoice = models.CharField(max_length=12,null=True,blank=True)
    stateTeFacturo = models.CharField(max_length=24,null=True,blank=True)
    nroInvoice = models.CharField(max_length=12,null=True,blank=True)
    typeItemsInvoice = models.CharField(max_length=12,null=True,blank=True)
    originInvoice = models.CharField(max_length=12,null=True,blank=True)
    asociatedQuotation = models.OneToOneField(quotationSystem,on_delete=models.CASCADE, blank=True, null=True)
    endpointInvoice = models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)


class guideSystem(models.Model):
    asociatedQuotation = models.OneToOneField(quotationSystem,on_delete=models.CASCADE, blank=True, null=True)
    asociatedBill = models.ForeignKey(billSystem, on_delete=models.SET_NULL, null=True, blank=True)
    asociatedInvoice = models.ForeignKey(invoiceSystem, on_delete=models.SET_NULL, null=True, blank=True)
    commentGuide = models.CharField(max_length=256, null=True, blank=True)
    dateGuide = models.DateField(null=True,blank=True)
    dateGivenGoods = models.DateField(null=True,blank=True)
    purposeTransportation = models.CharField(max_length=32,null=True,blank=True)
    modeTransportation = models.CharField(max_length=12,null=True,blank=True)
    extraWeight = models.CharField(max_length=8,null=True,blank=True)
    ubigeoClient = models.CharField(max_length=12,null=True,blank=True)
    deparmentDeparture = models.CharField(max_length=24,null=True,blank=True)
    provinceDeparture = models.CharField(max_length=24,null=True,blank=True)
    districtDeparture = models.CharField(max_length=24,null=True,blank=True)
    addressDeparture = models.CharField(max_length=256,null=True,blank=True)
    ubigeoDeparture = models.CharField(max_length=12,null=True,blank=True)
    razonSocialTranporter = models.CharField(max_length=256,null=True,blank=True)
    rucTransporter = models.CharField(max_length=12,null=True,blank=True)
    vehiclePlate = models.CharField(max_length=12,null=True,blank=True)
    dniDriver = models.CharField(max_length=12,null=True,blank=True)
    licenceDriver = models.CharField(max_length=12,null=True,blank=True)
    nameDriver = models.CharField(max_length=64,null=True,blank=True)
    stateGuide = models.CharField(max_length=12,null=True,blank=True)
    codeGuide = models.CharField(max_length=12,null=True,blank=True)
    stateTeFacturo = models.CharField(max_length=24,null=True,blank=True)
    nroGuide = models.CharField(max_length=12,null=True,blank=True)
    endpointGuide = models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

class creditNoteSystem(models.Model):
    asociatedBill = models.OneToOneField(billSystem,on_delete=models.CASCADE, blank=True, null=True)
    asociatedInvoice = models.OneToOneField(invoiceSystem,on_delete=models.CASCADE, blank=True, null=True)
    typeCreditNote = models.CharField(max_length=12,null=True,blank=True)
    stateCreditNote = models.CharField(max_length=12,null=True,blank=True)
    codeCreditNote = models.CharField(max_length=12,null=True,blank=True)
    stateTeFacturo = models.CharField(max_length=24,null=True,blank=True)
    dateCreditNote = models.DateField(null=True,blank=True)
    nroCreditNote = models.CharField(max_length=12,null=True,blank=True)
    originCreditNote = models.CharField(max_length=12,null=True,blank=True)
    endpointCreditNote = models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)


