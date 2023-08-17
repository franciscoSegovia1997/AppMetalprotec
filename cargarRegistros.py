import os
import django
import csv
import datetime

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from expensesMetalprotec.models import departmentCost, categoryCost, divisionCost, boxRegister, costRegister
from settingsMetalprotec.models import endpointSystem

endpointCost = endpointSystem.objects.get(serieFactura='F001')

print("Elimando todos los registros previos")
costRegister.objects.all().delete()
print("Registros eliminados")

print("Se cargaran los costos del sistema")

filename = 'registrosCostos.csv'
i = 0
with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:

        asociatedDivision = divisionCost.objects.filter(nameDivision=row[0])[0]
        asociatedBox = boxRegister.objects.filter(descriptionBox=row[1])[0]

        costRegister.objects.create(
            asociatedDivision=asociatedDivision,
            asociatedBox=asociatedBox,
            dateRegistered=datetime.datetime.strptime(row[2],'%d-%m-%Y'),
            rucCost=row[3],
            identificationCost=row[4],
            descriptionCost=row[5],
            quantityCost=[6],
            currencyCost=row[7],
            endpointCost=endpointCost
        )

        print(f"Se esta cargando el costo {i} en el sistema")
        i = i + 1

print(f"Archivo CSV '{filename}' cargado exitosamente.")