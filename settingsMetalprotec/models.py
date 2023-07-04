from django.db import models

# Create your models here.
class endpointSystem(models.Model):
    codeEndpoint=models.CharField(max_length=8,null=True,blank=True)
    serieCoti=models.CharField(max_length=8,null=True,blank=True)
    nroCoti=models.CharField(max_length=16,null=True,blank=True)
    serieGuia=models.CharField(max_length=8,null=True,blank=True)
    nroGuia=models.CharField(max_length=16,null=True,blank=True)
    serieFactura=models.CharField(max_length=8,null=True,blank=True)
    nroFactura=models.CharField(max_length=16,null=True,blank=True)
    serieBoleta=models.CharField(max_length=8,null=True,blank=True)
    nroBoleta=models.CharField(max_length=16,null=True,blank=True)
    serieNotaFactura=models.CharField(max_length=8,null=True,blank=True)
    nroNotaFactura=models.CharField(max_length=16,null=True,blank=True)
    serieNotaBoleta=models.CharField(max_length=8,null=True,blank=True)
    nroNotaBoleta=models.CharField(max_length=16,null=True,blank=True)

    def __str__(self):
        return f"{self.codeEndpoint}"