from django.db import models
from django.contrib.auth.models import User
from productsMetalprotec.models import productSystem, storeSystem
from salesMetalprotec.models import creditNoteSystem, billSystem, invoiceSystem
from django.contrib.postgres.fields import ArrayField
from settingsMetalprotec.models import endpointSystem

# Create your models here.
class incomingItemsRegisterInfo(models.Model):
    typeIncoming = models.CharField(max_length=32, blank=True, null=True)
    dateIncoming = models.DateField(blank=True, null=True)
    productCode = models.CharField(max_length=24, blank=True, null=True)
    nameStore = models.CharField(max_length=24,blank=True,null=True)
    quantityProduct = models.CharField(max_length=24,blank=True,null=True)
    lastStock = models.CharField(max_length=24,blank=True,null=True)
    newStock = models.CharField(max_length=24,blank=True,null=True)
    referenceIncome = models.CharField(max_length=24,blank=True,null=True)
    asociatedUserData = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL)
    asociatedProduct = models.ForeignKey(productSystem,blank=True, null=True, on_delete=models.SET_NULL)
    asociatedCreditNote = models.ForeignKey(creditNoteSystem,blank=True, null=True, on_delete=models.SET_NULL)
    asociatedStoreData = models.ForeignKey(storeSystem,blank=True, null=True, on_delete=models.SET_NULL)
    endpointIncoming = models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'{self.id}-{self.referenceIncome}'


class outcomingItemsRegisterInfo(models.Model):
    typeOutcoming = models.CharField(max_length=32, blank=True, null=True)
    dateOutcoming = models.DateField(blank=True, null=True)
    productCode = models.CharField(max_length=24, blank=True, null=True)
    nameStore = models.CharField(max_length=24,blank=True,null=True)
    quantityProduct = models.CharField(max_length=24,blank=True,null=True)
    lastStock = models.CharField(max_length=24,blank=True,null=True)
    newStock = models.CharField(max_length=24,blank=True,null=True)
    referenceOutcome = models.CharField(max_length=24,blank=True,null=True)
    asociatedUserData = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL)
    asociatedProduct = models.ForeignKey(productSystem,blank=True, null=True, on_delete=models.SET_NULL)
    asociatedBill = models.ForeignKey(billSystem,blank=True, null=True, on_delete=models.SET_NULL)
    asociatedInvoice = models.ForeignKey(invoiceSystem,blank=True, null=True, on_delete=models.SET_NULL)
    asociatedStoreData = models.ForeignKey(storeSystem,blank=True, null=True, on_delete=models.SET_NULL)
    endpointOutcoming = models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.id}-{self.referenceOutcome}'

class stockTakingData(models.Model):
    dateStockTaking = models.DateField(blank=True, null=True)
    codeStockTaking = models.CharField(max_length=12,blank=True,null=True)
    stateStockTaking = models.CharField(max_length=12,blank=True,null=True)
    storeStokTaking = models.CharField(max_length=12,blank=True,null=True)
    asociatedUserData = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL)
    asociatedStoreData = models.ForeignKey(storeSystem,blank=True, null=True, on_delete=models.SET_NULL)
    endpointStockTaking = models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.codeStockTaking}'

class infoStockTaking(models.Model):
    asociatedStockTaking = models.ForeignKey(stockTakingData,blank=True, null=True, on_delete=models.CASCADE)
    asociatedProsductInfo = models.ForeignKey(productSystem,on_delete=models.SET_NULL,blank=True,null=True)
    dataStockTakingInfo = ArrayField(models.CharField(max_length=128),null=True, blank=True)

    def __str__(self):
        return f'InfoStockTaking-{self.asociatedStockTaking.codeStockTaking}-{self.asociatedProsductInfo.codeProduct}'