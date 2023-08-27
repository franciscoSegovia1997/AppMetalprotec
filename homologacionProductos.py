import os
import django


# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from settingsMetalprotec.models import endpointSystem
from productsMetalprotec.models import productSystem

print("Se inicia con la migracion de productos")
endpointEnd2 = endpointSystem.objects.get(codeEndpoint='END-0002')
endpointEnd3 = endpointSystem.objects.get(codeEndpoint='END-0003')
productosEnd2 = productSystem.objects.filter(endpointProduct=endpointEnd2)
productosEnd3 = productSystem.objects.filter(endpointProduct=endpointEnd3)

print("Eliminando productos del punto de destino")
productosEnd3.delete()

print(f"Productos Totales : {len(productosEnd2)}")
print(f"Punto de origen : {endpointEnd2.codeEndpoint}")
print(f"Punto de destino : {endpointEnd3.codeEndpoint}")

totalProductos = len(productosEnd2)
i = 0
for productInfo in productosEnd2:
    productSystem.objects.create(
        nameProduct = productInfo.nameProduct,
        codeProduct = productInfo.codeProduct,
        codeSunatProduct =productInfo.codeSunatProduct,
        categoryProduct = productInfo.categoryProduct,
        subCategoryProduct = productInfo.subCategoryProduct,
        measureUnit = productInfo.measureUnit,
        currencyProduct = productInfo.currencyProduct,
        weightProduct = productInfo.weightProduct,
        pcnIGV = productInfo.pcnIGV,
        pccIGV = productInfo.pccIGV,
        pvnIGV = productInfo.pvnIGV,
        pvcIGV = productInfo.pvcIGV,
        kitProduct = productInfo.kitProduct,
        kitInfo = productInfo.kitInfo,
        endpointProduct=endpointEnd3
    )
    i = i + 1
    print(f"Se ha copiado el producto {i} de {totalProductos}")

print("Se ha finalizado con la migracion de productos")