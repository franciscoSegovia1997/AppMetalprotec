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
from salesMetalprotec.models import quotationSystem, quotationClientData,quotationSellerData,quotationProductData
from clientsMetalprotec.models import clientSystem
from productsMetalprotec.models import productSystem

quotationProductData.objects.all().delete()

filename = 'cargaMetalprotec/productosCotizaciones.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointQuotation = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        asociatedQuotation =quotationSystem.objects.get(codeQuotation=row[0])
        infoProducto = row
        del infoProducto[0]
        infoProducto = infoProducto[:9]
        if row[-1] == '0':
            infoProducto.append('0')
        else:
            infoProducto.append('1')

        infoProducto[4] = infoProducto[4].upper()

        try:
            asociatedProduct = productSystem.objects.get(codeProduct=infoProducto[2])
            infoProducto[0] = str(asociatedProduct.id)

            quotationProductData.objects.create(
                asociatedQuotation=asociatedQuotation,
                asociatedProduct=asociatedProduct,
                dataProductQuotation=infoProducto,
                weightProduct=asociatedProduct.weightProduct
            )
        except:
            infoProducto[0] = '0'

            quotationProductData.objects.create(
                asociatedQuotation=asociatedQuotation,
                dataProductQuotation=infoProducto,
                weightProduct=asociatedProduct.weightProduct
            )