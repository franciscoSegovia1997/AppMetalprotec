import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from expensesMetalprotec.models import departmentCost
from settingsMetalprotec.models import endpointSystem

endpointDeparment = endpointSystem.objects.get(serieFactura='F001')

print(f"Se cargaran los departamentos del sistema")

filename = 'allDepartments.csv'

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        departmentCost.objects.create(
            nameDeparment=row[0],
            endpointDeparment=endpointDeparment
        )

print(f"Archivo CSV '{filename}' cargado exitosamente.")