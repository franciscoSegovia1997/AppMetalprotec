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

filename = 'cargaMetalprotec/productosMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointProduct = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        productSystem.objects.create(
            nameProduct=row[0],
            codeProduct=row[1],
            codeSunatProduct=row[2],
            categoryProduct=row[3],
            subCategoryProduct=row[4],
            measureUnit=row[5],
            currencyProduct=row[6],
            weightProduct=row[7],
            pcnIGV=row[8],
            pccIGV=row[9],
            pvnIGV=row[10],
            pvcIGV=row[11],
            kitProduct=row[12],
            endpointProduct=endpointProduct
        )

print('Carga finalizada exitosamente')