from django.db import models
from settingsMetalprotec.models import endpointSystem



# Create your models here.
class clientSystem(models.Model):
    documentClient = models.CharField(max_length=12, null=True,blank=True)
    identificationClient = models.CharField(max_length=256, null=True,blank=True)
    typeClient = models.CharField(max_length=10, null=True, blank=True)
    emailClient = models.CharField(max_length=48, null=True, blank=True)
    contactClient = models.CharField(max_length=64, null=True, blank=True)
    phoneClient = models.CharField(max_length=16, null=True, blank=True)
    legalAddressClient = models.CharField(max_length=256, null=True, blank=True)
    enabledCommission = models.CharField(max_length=6, null=True, blank=True)
    endpointClient = models.ForeignKey(endpointSystem, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.identificationClient}'
    
class addressClient(models.Model):
    deliveryAddress = models.CharField(max_length=256, null=True, blank=True)
    asociatedClient = models.ForeignKey(clientSystem,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.deliveryAddress}'