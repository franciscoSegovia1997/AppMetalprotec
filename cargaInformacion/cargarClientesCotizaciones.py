import os
import django
import csv
import datetime

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser
from servicesMetalprotec.models import serviceSystem
from salesMetalprotec.models import quotationSystem, quotationClientData
from clientsMetalprotec.models import clientSystem

quotationClientData.objects.all().delete()

filename = 'cargaMetalprotec/cotizacionesClientesMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointQuotation = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        asociatedQuotation =quotationSystem.objects.get(codeQuotation=row[0])
        infoCliente = row
        del infoCliente[0]

        asociatedClient = clientSystem.objects.get(documentClient=infoCliente[2])
        infoCliente[0] = str(asociatedClient.id)

        quotationClientData.objects.create(
            asociatedQuotation=asociatedQuotation,
            asociatedClient=asociatedClient,
            dataClientQuotation=infoCliente
        )
