#Verificacion de codigo:

import os
import django


# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from settingsMetalprotec.models import endpointSystem
from productsMetalprotec.models import productSystem

print("Se inicia con la verificacion de codigos unicos por producto")
print("Para el almacen de trujillo : ")
endpointEnd3 = endpointSystem.objects.get(codeEndpoint='END-0003')
productosEnd3 = productSystem.objects.filter(endpointProduct=endpointEnd3)

print(f"Productos Totales : {len(productosEnd3)}")

codeProductos = []
codigosRepetidos = []
i = 1
for productInfo in productosEnd3:
    print(f"Procesando producto {i} de {len(productosEnd3)}")
    if productInfo.codeProduct in codeProductos:
        print(f"------------------------- El codigo {productInfo.codeProduct} es repetido")
        codigosRepetidos.append(productInfo.codeProduct)
    else:
        codeProductos.append(productInfo.codeProduct)
        print('ProductoProcesado')
    i = i + 1

print(f"Codigos repetidos en trujillo : {codigosRepetidos}")