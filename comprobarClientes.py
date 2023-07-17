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
from clientsMetalprotec.models import clientSystem

clientesTotales = clientSystem.objects.all()

i = 0
j = 0
for clienteInfo in clientesTotales:
    unico = len(clientSystem.objects.filter(documentClient=clienteInfo.documentClient))
    if unico == 1:
        i = i + 1
    else:
        clienteInfo.delete()
        j = j + 1
        print(f"{clienteInfo.identificationClient} - {clienteInfo.documentClient}")

print(f"Se tienen {i} clientes unicos")
print(f"Se tienen {j} clientes repetidos")
print(f"Se tienen {i + j} clientes en total")
