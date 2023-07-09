from django.db import models
from settingsMetalprotec.models import endpointSystem

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