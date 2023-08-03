import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser
from productsMetalprotec.models import productSystem

filename = 'cargaMetalprotec/productoKitMetalprotec.csv'
filename2 = 'cargaMetalprotec/infoKitMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointProduct = usuarioRaiz.extendeduser.endpointUser

datosKitsProductos = []
infoKitsProductos = []
with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        datosKitsProductos.append(row)


with open(filename2, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        infoKitsProductos.append(row)


i = 0
while i < len(datosKitsProductos):
    productoCreado = productSystem.objects.create(
        nameProduct =datosKitsProductos[i][0],
        codeProduct =datosKitsProductos[i][1],
        codeSunatProduct =datosKitsProductos[i][2],
        categoryProduct =datosKitsProductos[i][3],
        subCategoryProduct =datosKitsProductos[i][4],
        measureUnit =datosKitsProductos[i][5],
        currencyProduct =datosKitsProductos[i][6],
        weightProduct =datosKitsProductos[i][7],
        pcnIGV =datosKitsProductos[i][8],
        pccIGV =datosKitsProductos[i][9],
        pvnIGV =datosKitsProductos[i][10],
        pvcIGV =datosKitsProductos[i][11],
        kitProduct =datosKitsProductos[i][12],
        endpointProduct =endpointProduct
    )

    productoInfoKit = productSystem.objects.filter(codeProduct=infoKitsProductos[i][0])[0]
    productoInfoKit1 = productSystem.objects.filter(codeProduct=infoKitsProductos[i][2])[0]

    productoCreado.kitInfo = []
    productoCreado.save()
    productoCreado.kitInfo.append([productoInfoKit.id,infoKitsProductos[i][1]])
    productoCreado.kitInfo.append([productoInfoKit1.id,infoKitsProductos[i][3]])
    productoCreado.save()
    i = i + 1



print(datosKitsProductos[23][1])
print(infoKitsProductos[2][3])


print('Carga finalizada exitosamente')