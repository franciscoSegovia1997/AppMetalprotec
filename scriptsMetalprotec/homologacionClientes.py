import os
import django


# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from settingsMetalprotec.models import endpointSystem
from clientsMetalprotec.models import clientSystem

print("Se inicia con la migracion de clientes")
endpointEnd2 = endpointSystem.objects.get(codeEndpoint='END-0002')
endpointEnd3 = endpointSystem.objects.get(codeEndpoint='END-0003')
clientesEnd2 = clientSystem.objects.filter(endpointClient=endpointEnd2)
clientesEnd3 = clientSystem.objects.filter(endpointClient=endpointEnd3)

print("Eliminando clientes del punto de destino")
clientesEnd3.delete()

print(f"Clientes Totales : {len(clientesEnd2)}")
print(f"Punto de origen : {endpointEnd2.codeEndpoint}")
print(f"Punto de destino : {endpointEnd3.codeEndpoint}")

totalClientes = len(clientesEnd2)
i = 0
for clienteInfo in clientesEnd2:
    clientSystem.objects.create(
        documentClient = clienteInfo.documentClient,
        identificationClient = clienteInfo.identificationClient,
        typeClient = clienteInfo.typeClient,
        emailClient = clienteInfo.emailClient,
        contactClient = clienteInfo.contactClient,
        phoneClient = clienteInfo.phoneClient,
        legalAddressClient = clienteInfo.legalAddressClient,
        enabledCommission = clienteInfo.enabledCommission,
        endpointClient = endpointEnd3
    )
    i = i + 1
    print(f"Se ha copiado el cliente {i} de {totalClientes}")

print("Se ha finalizado con la migracion de clientes")