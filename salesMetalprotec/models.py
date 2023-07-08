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
    relatedDocumentQuotation = models.CharField(max_length=12, null=True, blank=True)
    commentQuotation = models.CharField(max_length=256, null=True, blank=True)
    quotesQuotation = models.CharField(max_length=4, null=True, blank=True)
    expirationCredit = models.CharField(max_length=4,null=True,blank=True)
    expirationQuotation = models.CharField(max_length=4,null=True,blank=True)
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

class quotationServiceData(models.Model):
    asociatedQuotation = models.ForeignKey(quotationSystem,on_delete=models.CASCADE, blank=True, null=True)
    asociatedService = models.ForeignKey(serviceSystem, on_delete=models.SET_NULL, null=True, blank=True)
    dataServiceQuotation = ArrayField(models.CharField(max_length=256),null=True,blank=True)


