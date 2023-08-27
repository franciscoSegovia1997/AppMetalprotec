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
from financeMetalprotec.models import bankOperation, bankSystem

endpointOperation = endpointSystem.objects.get(serieFactura='F001')

print("Elimando todos los registros bancarios previos")
bankOperation.objects.all().delete()
print("Registros eliminados")

print("Se cargaran los costos del sistema")

filename = 'registrosBancosInfo.csv'
i = 0
with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:

        bankInfo = bankSystem.objects.filter(nameBank=row[2]).filter(currencyBank=row[1])[0]

        bankOperation.objects.create(
            dateOperation=datetime.datetime.strptime(row[0],'%d-%m-%Y'),
            currencyOperation=row[1],
            detailOperation=row[3],
            moneyOperation=row[4],
            numberOperation=row[5],
            typeOperation=row[6],
            stateOperation=row[7],
            nameClient=row[8],
            nameSeller=row[9],
            codeDocument=row[10],
            codeQuotation=row[12],
            asociatedBank=bankInfo,
            endpointOperation=endpointOperation,
        )
        print(f"Se esta cargando el registro {i} en el sistema")
        i = i + 1

print(f"Archivo CSV '{filename}' cargado exitosamente.")