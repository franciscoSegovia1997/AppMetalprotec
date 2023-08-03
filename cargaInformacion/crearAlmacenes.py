import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser
from productsMetalprotec.models import productSystem, storeSystem, storexproductSystem

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointProduct = usuarioRaiz.extendeduser.endpointUser

productosTotales = productSystem.objects.all()
storesTotales = storeSystem.objects.all()

print(f"Total de productos : {len(productosTotales)}")

i = 0
for produntoInfo in productosTotales:
    for storeInfo in storesTotales:
        storexproductSystem.objects.create(
            quantityProduct = '0.00',
            asociatedProduct=produntoInfo,
            asociatedStore=storeInfo,
        )
    i = i + 1

print(f"Productos sin ningun almacen : {i}")