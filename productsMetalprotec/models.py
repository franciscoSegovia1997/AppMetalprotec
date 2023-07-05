from django.db import models
from settingsMetalprotec.models import endpointSystem
from decimal import Decimal, DecimalException,getcontext

getcontext().prec = 10

class storeSystem(models.Model):
    nameStore = models.CharField(max_length=16,null=True,blank=True)
    dateCreation = models.DateField(null=True,blank=True)
    endpointStore=models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

# Create your models here.
class productSystem(models.Model):
    nameProduct = models.CharField(max_length=64,null=True,blank=True)
    codeProduct = models.CharField(max_length=24,null=True,blank=True)
    codeSunatProduct = models.CharField(max_length=24,null=True,blank=True)
    categoryProduct = models.CharField(max_length=16,null=True,blank=True)
    subCategoryProduct = models.CharField(max_length=16,null=True,blank=True)
    measureUnit = models.CharField(max_length=16,null=True,blank=True)
    currencyProduct = models.CharField(max_length=16,null=True,blank=True)
    weightProduct = models.CharField(max_length=16,null=True,blank=True)
    pcnIGV = models.CharField(max_length=16,null=True,blank=True)
    pccIGV = models.CharField(max_length=16,null=True,blank=True)
    pvnIGV = models.CharField(max_length=16,null=True,blank=True)
    pvcIGV = models.CharField(max_length=16,null=True,blank=True)
    endpointProduct=models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nameProduct}-{self.codeProduct}'

    def getStockTotal(self):
        stockProducts = self.storexproductsystem_set.all()
        if len(stockProducts) == 0:
            return '0.00'
        else:
            totalStock = Decimal(0.00)
            for stock in stockProducts:
                totalStock = Decimal(totalStock) + Decimal(stock.quantityProduct)
            totalStock = str(Decimal('%.2f' % (Decimal(totalStock))))
            return totalStock

class storexproductSystem(models.Model):
    quantityProduct = models.CharField(max_length=16,null=True,blank=True)
    asociatedProduct = models.ForeignKey(productSystem, on_delete=models.CASCADE, null=True, blank=True)
    asociatedStore = models.ForeignKey(storeSystem, on_delete=models.CASCADE, null=True, blank=True)