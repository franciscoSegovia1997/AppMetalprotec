from django.db import models
from settingsMetalprotec.models import endpointSystem
from salesMetalprotec.models import billSystem, invoiceSystem
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class bankSystem(models.Model):
    nameBank = models.CharField(max_length=12,blank=True,null=True)
    currencyBank = models.CharField(max_length=10,blank=True,null=True)
    accountNumber = models.CharField(max_length=32,blank=True,null=True)
    moneyBank = models.CharField(max_length=12,blank=True,null=True)
    endpointBank = models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)

class paymentSystem(models.Model):
    datePayment = models.DateField(blank=True, null=True)
    nameBankPayment = models.CharField(max_length=12, blank=True, null=True)
    currencyPayment = models.CharField(max_length=12, blank=True, null=True)
    operationNumber = models.CharField(max_length=24, blank=True, null=True)
    nameClient = models.CharField(max_length=128, blank=True, null=True)
    statePayment = models.CharField(max_length=12, blank=True, null=True)
    codeDocument = models.CharField(max_length=12, blank=True, null=True)
    codeGuide = models.CharField(max_length=12, blank=True, null=True)
    codeQuotation = models.CharField(max_length=12, blank=True, null=True)
    codeSeller = models.CharField(max_length=12, blank=True, null=True)
    typeDocumentPayment = models.CharField(max_length=12, blank=True, null=True)
    asociatedBank = models.ForeignKey(bankSystem, null=True, blank=True, on_delete=models.SET_NULL)
    asociatedBill = models.ForeignKey(billSystem, null=True, blank=True, on_delete=models.SET_NULL)
    asociatedInvoice = models.ForeignKey(invoiceSystem, null=True, blank=True, on_delete=models.SET_NULL)
    endpointPayment = models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

class bankOperation(models.Model):
    dateOperation = models.DateField(blank=True, null=True)
    currencyOperation = models.CharField(max_length=10, blank=True, null=True)
    detailOperation = models.CharField(max_length=64, blank=True, null=True)
    moneyOperation = models.CharField(max_length=12, blank=True, null=True)
    numberOperation = models.CharField(max_length=16, blank=True, null=True)
    typeOperation = models.CharField(max_length=12, blank=True, null=True)
    stateOperation = models.CharField(max_length=12, blank=True, null=True)
    nameClient = models.CharField(max_length=128, blank=True, null=True)
    nameSeller = models.CharField(max_length=64, blank=True, null=True)
    codeDocument = models.CharField(max_length=12, blank=True, null=True)
    codeQuotation = models.CharField(max_length=12, blank=True, null=True)
    asociatedBill = models.ForeignKey(billSystem, null=True, blank=True, on_delete=models.SET_NULL)
    asociatedInvoice = models.ForeignKey(invoiceSystem, null=True, blank=True, on_delete=models.SET_NULL)
    asociatedUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    asociatedPayment = models.ForeignKey(paymentSystem, on_delete=models.SET_NULL, null=True, blank=True)
    asociatedBank = models.ForeignKey(bankSystem, on_delete=models.CASCADE, null=True, blank=True)
    endpointOperation = models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

class settingsComission(models.Model):
    dateRegistered = models.DateField(blank=True, null=True)
    igvIncluded = models.CharField(max_length=10, blank=True, null=True)
    percentageComision = models.CharField(max_length=10, blank=True, null=True)
    typeComission = models.CharField(max_length=12, blank=True, null=True)
    comissionCode = models.CharField(max_length=12, blank=True, null=True)
    asociatedUsers = ArrayField(models.CharField(max_length=8),null=True, blank=True)
    endpointComission = models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)