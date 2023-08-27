import os
import django
from settingsMetalprotec.models import endpointSystem
from productsMetalprotec.models import productSystem

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

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
    


filename = 'cargaMetalprotec/productosMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointProduct = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        productSystem.objects.create(
            nameProduct=row[0],
            codeProduct=row[1],
            codeSunatProduct=row[2],
            categoryProduct=row[3],
            subCategoryProduct=row[4],
            measureUnit=row[5],
            currencyProduct=row[6],
            weightProduct=row[7],
            pcnIGV=row[8],
            pccIGV=row[9],
            pvnIGV=row[10],
            pvcIGV=row[11],
            kitProduct=row[12],
            endpointProduct=endpointProduct
        )

print('Carga finalizada exitosamente')