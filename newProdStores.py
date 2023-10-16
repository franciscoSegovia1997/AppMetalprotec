#Creacion de productos en todos los almacenes

import os
import django


# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from settingsMetalprotec.models import endpointSystem
from productsMetalprotec.models import productSystem, storeSystem, storexproductSystem

print("Se inicia con la migracion de productos")
endpointEnd2 = endpointSystem.objects.get(codeEndpoint='END-0002')
endpointEnd3 = endpointSystem.objects.get(codeEndpoint='END-0003')
productosEnd2 = productSystem.objects.filter(endpointProduct=endpointEnd2)
productosEnd3 = productSystem.objects.filter(endpointProduct=endpointEnd3)

print(f"Productos Totales de chimbote : {len(productosEnd2)}")
print(f"Productos Totales de trujillo : {len(productosEnd3)}")

codigosChimbote = []
codigosTrujillo = []

print("Obtencion de los codigos de cada Almacen : ")
print("Empezando con chimbote : ")
for productInfo in productosEnd2:
    codigosChimbote.append(productInfo.codeProduct)
print("Chimbote finalizado")
print(f"Se tienen {len(codigosChimbote)} productos en chimbote")

print("Empezando con trujillo : ")
for productInfo in productosEnd3:
    codigosTrujillo.append(productInfo.codeProduct)
print("Trujillo finalizado")
print(f"Se tienen {len(codigosTrujillo)} productos en trujillo")

print("CREANDO PRODUCTOS NUEVOS EN TRUJILLO :")
for productInfo in productosEnd2:
    if productInfo.codeProduct not in codigosTrujillo:
        print(f"Falta el codigo: {productInfo.codeProduct} en Trujillo")
"""
        productObjectCreated = productSystem.objects.create(
            nameProduct=productInfo.nameProduct,
            codeProduct=productInfo.codeProduct,
            codeSunatProduct=productInfo.codeSunatProduct,
            categoryProduct=productInfo.categoryProduct,
            subCategoryProduct=productInfo.subCategoryProduct,
            measureUnit=productInfo.measureUnit,
            weightProduct=productInfo.weightProduct,
            currencyProduct=productInfo.currencyProduct,
            pvnIGV=productInfo.pvnIGV,
            pvcIGV=productInfo.pvcIGV,
            pcnIGV=productInfo.pcnIGV,
            pccIGV=productInfo.pccIGV,
            kitProduct=productInfo.kitProduct,
            kitInfo=productInfo.kitInfo,
            endpointProduct=endpointEnd3,
        )

        allStoreSystem = storeSystem.objects.filter(endpointStore=endpointEnd3)
        for storeInfo in allStoreSystem:
            storexproductSystem.objects.create(
                quantityProduct='0',
                asociatedProduct=productObjectCreated,
                asociatedStore=storeInfo,
            )
        print(f"Producto {productInfo.codeProduct} creado en trujillo")
"""

print("CREANDO PRODUCTOS NUEVOS EN CHIMBOTE :")
for productInfo in productosEnd3:
    if productInfo.codeProduct not in codigosChimbote:
        print(f"Falta el codigo: {productInfo.codeProduct} en Chimbote")
"""
        productObjectCreated = productSystem.objects.create(
            nameProduct=productInfo.nameProduct,
            codeProduct=productInfo.codeProduct,
            codeSunatProduct=productInfo.codeSunatProduct,
            categoryProduct=productInfo.categoryProduct,
            subCategoryProduct=productInfo.subCategoryProduct,
            measureUnit=productInfo.measureUnit,
            weightProduct=productInfo.weightProduct,
            currencyProduct=productInfo.currencyProduct,
            pvnIGV=productInfo.pvnIGV,
            pvcIGV=productInfo.pvcIGV,
            pcnIGV=productInfo.pcnIGV,
            pccIGV=productInfo.pccIGV,
            kitProduct=productInfo.kitProduct,
            kitInfo=productInfo.kitInfo,
            endpointProduct=endpointEnd2,
        )

        allStoreSystem = storeSystem.objects.filter(endpointStore=endpointEnd2)
        for storeInfo in allStoreSystem:
            storexproductSystem.objects.create(
                quantityProduct='0',
                asociatedProduct=productObjectCreated,
                asociatedStore=storeInfo,
            )
        print(f"Producto {productInfo.codeProduct} creado en chimbote")
"""