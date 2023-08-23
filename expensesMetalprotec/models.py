from django.db import models
from settingsMetalprotec.models import endpointSystem
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class departmentCost(models.Model):
    nameDeparment = models.CharField(max_length=32,blank=True,null=True)
    endpointDeparment=models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nameDeparment

class categoryCost(models.Model):
    nameCategory = models.CharField(max_length=32, null=True, blank=True)
    asociatedDeparment = models.ForeignKey(departmentCost, on_delete=models.CASCADE, null=True, blank=True)
    endpointCategory=models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nameCategory

class divisionCost(models.Model):
    asociatedCategory = models.ForeignKey(categoryCost, on_delete=models.CASCADE,null=True,blank=True)
    nameDivision = models.CharField(max_length=32, null=True, blank=True)
    typeCost = models.CharField(max_length=16, null=True, blank=True)
    behavior = models.CharField(max_length=16, null=True, blank=True)
    operativeCost = models.CharField(max_length=8, null=True, blank=True)
    endpointDivision=models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nameDivision
    
class boxRegister(models.Model):
    descriptionBox=models.CharField(max_length=32, null=True, blank=True)
    valueBox=models.CharField(max_length=16,null=True, blank=True)
    creationDate=models.DateField(null=True, blank=True)
    currencyBox=models.CharField(max_length=8, null=True, blank=True)
    endpointBox=models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.descriptionBox


class costRegister(models.Model):
    asociatedDivision=models.ForeignKey(divisionCost,on_delete=models.CASCADE,null=True,blank=True)
    asociatedBox=models.ForeignKey(boxRegister,null=True,blank=True,on_delete=models.SET_NULL)
    dateRegistered=models.DateField(null=True, blank=True)
    documentCost=models.CharField(max_length=16,null=True,blank=True)
    rucCost=models.CharField(max_length=12,null=True,blank=True)
    identificationCost=models.CharField(max_length=64,null=True,blank=True)
    descriptionCost=models.CharField(max_length=64,null=True,blank=True)
    quantityCost=models.CharField(max_length=12,null=True,blank=True)
    currencyCost=models.CharField(max_length=8,null=True,blank=True)
    endpointCost=models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.descriptionCost
    
class cashIncome(models.Model):
    asociatedBox=models.ForeignKey(boxRegister,null=True,blank=True,on_delete=models.SET_NULL)
    dateRegistered=models.DateField(null=True, blank=True)
    descriptionIncome=models.CharField(max_length=48,null=True, blank=True)
    quantityIncome=models.CharField(max_length=12,null=True, blank=True)
    endpointIncome=models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.descriptionIncome

class ordenCompraMetalprotec(models.Model):
    rucProveedor=models.CharField(max_length=32, null=True, blank=True)
    fechaEmision=models.DateField(null=True, blank=True)
    condicionOrden=models.CharField(max_length=32, null=True, blank=True)
    codigoOrden=models.CharField(max_length=32, null=True, blank=True)
    direccionProveedor=models.CharField(max_length=128, null=True, blank=True)
    nombreProveedor=models.CharField(max_length=64, null=True, blank=True)
    ciudadCliente=models.CharField(max_length=32, null=True, blank=True)
    destinoCliente=models.CharField(max_length=128, null=True, blank=True)
    atencionCliente=models.CharField(max_length=64, null=True, blank=True)
    monedaOrden=models.CharField(max_length=12, null=True, blank=True)
    productosOrden=ArrayField(ArrayField(models.CharField(max_length=64),null=True, blank=True),null=True,blank=True)
    tcCompraOrden=models.CharField(max_length=8, null=True, blank=True)
    tcVentaOrden=models.CharField(max_length=8, null=True, blank=True)
    mostrarDescuento=models.CharField(max_length=8, null=True, blank=True)
    mostrarVU=models.CharField(max_length=8, null=True, blank=True)
    endpointOrden=models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)