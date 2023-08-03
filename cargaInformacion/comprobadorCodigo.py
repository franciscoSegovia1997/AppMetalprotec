import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser
from productsMetalprotec.models import productSystem


usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointProduct = usuarioRaiz.extendeduser.endpointUser

productosTotales = productSystem.objects.all()

i = 0
j = 0
k = 0
l = 0
for productoInfo in productosTotales:
    informacionProducto = len(productSystem.objects.filter(codeProduct=productoInfo.codeProduct))
    if informacionProducto == 1:
        i = i + 1
    elif informacionProducto == 0:
        j = j + 1
    else:
        l = l + 1
        print(f"{productoInfo.nameProduct} - {productoInfo.codeProduct}")
        productoInfo.delete()
    k = k + 1

print(f"En total se tienen {k} productos en todos el sistema")
print(f"Productos con codigo unico : {i}")
print(f"Productos con codigo repetido : {l}")
print(f"Codigos que no pertenecen a ningun producto : {j}")