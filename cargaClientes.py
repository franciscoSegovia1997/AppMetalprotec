import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser
from clientsMetalprotec.models import clientSystem

filename = 'cargaMetalprotec/clientesMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointCliente = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        clientSystem.objects.create(
            documentClient=row[2],
            identificationClient=row[1],
            typeClient=row[0],
            emailClient=row[3],
            contactClient=row[4],
            phoneClient=row[5],
            legalAddressClient=row[6],
            enabledCommission=row[7],
            endpointClient=endpointCliente
        )

print('Carga finalizada exitosamente')