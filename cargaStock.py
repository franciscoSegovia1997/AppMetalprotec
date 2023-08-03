#Primera etapa: Comprobar codigos

import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from productsMetalprotec.models import productSystem, storeSystem, storexproductSystem

filename = 'infoStock.csv'

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(f"Codigo a inspeccionar : {row[0]}")
        try:
            infoProducto = productSystem.objects.get(codeProduct=row[0])
            print(f"CODIGO UNICO - {row[0]} CON STOCK {row[1]}")
        except:
            print(f"CODIGO REPETIDO!! - {row[0]}")

#SEGUNDA ETAPA : ELIMINAR EL STOCK ACTUAL

totalStock = storexproductSystem.objects.all()
for stockInfo in totalStock:
    print(f"MODIFICANDO EL STOCK DEL PRODUCTO: {stockInfo.asociatedProduct.nameProduct} - EN EL ALMACEN: {stockInfo.asociatedStore.nameStore}")
    stockInfo.quantityProduct = '0.00'
    stockInfo.save()
    print("STOCK MODIFICADO")