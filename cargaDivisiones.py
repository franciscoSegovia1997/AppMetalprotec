import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from expensesMetalprotec.models import departmentCost, categoryCost, divisionCost
from settingsMetalprotec.models import endpointSystem

endpointDivision = endpointSystem.objects.get(serieFactura='F001')

print(f"Se cargaran las divisiones del sistema")

filename = 'todoDivisiones.csv'

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        asociatedCategory = categoryCost.objects.get(nameCategory=row[4])
        divisionCost.objects.create(
            nameDivision=row[0],
            typeCost=row[1],
            behavior=row[2],
            operativeCost=row[3],
            asociatedCategory=asociatedCategory,
            endpointCategory=endpointCategory
        )

print(f"Archivo CSV '{filename}' cargado exitosamente.")