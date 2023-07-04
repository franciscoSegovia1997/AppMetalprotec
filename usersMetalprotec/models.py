from django.db import models
from django.contrib.auth.models import User
from settingsMetalprotec.models import endpointSystem

# Create your models here.
class rolesxUser(models.Model):
    nameRole = models.CharField(max_length=32)

    def __str__(self):
        return self.nameRole


class extendedUser(models.Model):
    asociatedUser = models.OneToOneField(User,on_delete=models.CASCADE)
    codeUser = models.CharField(max_length=16, default='<NoCode>')
    nameUser = models.CharField(max_length=32, default='<NoName>')
    lastnameUser = models.CharField(max_length=32, default='<NoLastName>')
    phoneUser = models.CharField(max_length=12, default='<NoPhone>')
    roleUser = models.ForeignKey(rolesxUser,on_delete=models.SET_NULL,null=True, blank=True)
    endpointUser = models.ForeignKey(endpointSystem, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nameUser} {self.lastnameUser}"

