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