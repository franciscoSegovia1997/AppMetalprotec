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

        totalDivisiones = divisionCost.objects.filter(nameDivision=row[0]).filter(asociatedCategory__nameCategory=row[1]).filter(asociatedCategory__asociatedDeparment__nameDeparment=row[2])
        asociatedDivision = totalDivisiones[0]
        asociatedBox = boxRegister.objects.get(descriptionBox=row[3])

        costRegister.objects.create(
            asociatedDivision=asociatedDivision,
            asociatedBox=asociatedBox,
            dateRegistered=datetime.datetime.strptime(row[4],'%d-%m-%Y'),
            rucCost=row[5],
            identificationCost=row[6],
            descriptionCost=row[7],
            quantityCost=row[8],
            currencyCost=row[9],
            endpointCost=endpointCost
        )

        print(f"Se esta cargando el costo {i} en el sistema - Concepto = {row[7]} - TotalDivisiones = {len(totalDivisiones)} - Division={asociatedDivision.nameDivision}, Categoria={asociatedDivision.asociatedCategory.nameCategory}, Departamento={asociatedDivision.asociatedCategory.asociatedDeparment.nameDeparment}")
        i = i + 1

print(f"Archivo CSV '{filename}' cargado exitosamente.")