import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from expensesMetalprotec.models import departmentCost, categoryCost
from settingsMetalprotec.models import endpointSystem

endpointCategory = endpointSystem.objects.get(serieFactura='F001')

print(f"Se cargaran las categorias del sistema")

filename = 'todoCategorias.csv'

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        asociatedDeparment = departmentCost.objects.get(nameDeparment=row[1])
        categoryCost.objects.create(
            nameCategory=row[0],
            asociatedDeparment=asociatedDeparment,
            endpointCategory=endpointCategory
        )

print(f"Archivo CSV '{filename}' cargado exitosamente.")