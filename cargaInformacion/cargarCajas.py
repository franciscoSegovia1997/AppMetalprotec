import os
import django
import csv
import datetime

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from expensesMetalprotec.models import departmentCost, categoryCost, divisionCost, boxRegister
from settingsMetalprotec.models import endpointSystem

endpointBox = endpointSystem.objects.get(serieFactura='F001')

print(f"Se cargaran las cajas del sistema")

filename = 'cajasActuales.csv'

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        boxRegister.objects.create(
            descriptionBox=row[0],
            valueBox=row[1],
            creationDate=datetime.datetime.strptime(row[2],'%d-%m-%Y'),
            currencyBox=row[3],
            endpointBox=endpointBox,
        )

print(f"Archivo CSV '{filename}' cargado exitosamente.")