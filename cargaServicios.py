import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser
from servicesMetalprotec.models import serviceSystem

filename = 'cargaMetalprotec/servicesMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointService = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        serviceSystem.objects.create(
            nameService=row[0],
            categoryService=row[1],
            subCategoryService=row[2],
            currencyService=row[3],
            measureUnit=row[4],
            pvnIGV=row[5],
            pvcIGV=row[6],
            endpointService=endpointService
        )

print('Carga finalizada exitosamente')