from django.db import models
from settingsMetalprotec.models import endpointSystem

# Create your models here.
class serviceSystem(models.Model):
    nameService = models.CharField(max_length=64,null=True,blank=True)
    categoryService = models.CharField(max_length=16,null=True,blank=True)
    subCategoryService = models.CharField(max_length=16,null=True,blank=True)
    measureUnit = models.CharField(max_length=16,null=True,blank=True)
    pvnIGV = models.CharField(max_length=16,null=True,blank=True)
    pvcIGV = models.CharField(max_length=16,null=True,blank=True)
    endpointService = models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return f"{self.nameService}"