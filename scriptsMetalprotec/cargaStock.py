#Primera etapa: Comprobar codigos

import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from productsMetalprotec.models import productSystem, storeSystem, storexproductSystem
from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointProduct = usuarioRaiz.extendeduser.endpointUser

filename = 'newStock.csv'

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(f"Codigo a inspeccionar : {row[0]}")
        try:
            infoProducto = productSystem.objects.filter(endpointProduct=endpointProduct).get(codeProduct=row[0])
            print(f"CODIGO UNICO - {row[0]} CON STOCK {row[1]}")
        except:
            print(f"CODIGO REPETIDO!! - {row[0]}")

#SEGUNDA ETAPA : ELIMINAR EL STOCK ACTUAL

totalStock = storexproductSystem.objects.all().filter(asociatedStore__nameStore='CHIMBOTE')
for stockInfo in totalStock:
    if stockInfo.asociatedStore.nameStore == 'CHIMBOTE':
        print(f"MODIFICANDO EL STOCK DEL PRODUCTO: {stockInfo.asociatedProduct.nameProduct} - EN EL ALMACEN: {stockInfo.asociatedStore.nameStore}")
        stockInfo.quantityProduct = '0.00'
        stockInfo.save()
        print("STOCK MODIFICADO")

#ACTUALIZAR STOCK


with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(f"Codigo a inspeccionar : {row[0]}")
        try:
            infoProducto = productSystem.objects.filter(endpointProduct=endpointProduct).get(codeProduct=row[0])
            print(f"CODIGO UNICO - {row[0]} CON STOCK {row[1]}.00")
            objProducto = infoProducto.storexproductsystem_set.all().get(asociatedStore__nameStore='CHIMBOTE')
            objProducto.quantityProduct = f"{row[1]}.00"
            objProducto.save()
            print(f"DATOS: {objProducto.quantityProduct} - {objProducto.asociatedStore.nameStore} - {objProducto.asociatedProduct.nameProduct}")
        except:
            print(f"CODIGO REPETIDO!! - {row[0]}")

print(f"Carga del archivo {filename} finalizado")