import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from salesMetalprotec.models import invoiceSystem

boletasTotales = invoiceSystem.objects.all()

arregloBoletas = []
for boletaInfo in boletasTotales:
    if boletaInfo.asociatedQuotation is not None:
        codigo = boletaInfo.asociatedQuotation.codeQuotation
    else:
        codigo = boletaInfo.guidesystem_set.all()[0].codeGuide

    datosBoleta = [
        boletaInfo.commentInvoice,
        boletaInfo.dateInvoice,
        boletaInfo.relatedDocumentInvoice,
        boletaInfo.erBuy,
        boletaInfo.erSel,
        boletaInfo.currencyInvoice,
        boletaInfo.stateInvoice,
        boletaInfo.codeInvoice,
        boletaInfo.stateTeFacturo,
        boletaInfo.nroInvoice,
        boletaInfo.typeItemsInvoice,
        boletaInfo.originInvoice,
        codigo
    ]
    arregloBoletas.append(datosBoleta)

filename = 'boletasMetalprotec.csv'

with open(filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(arregloBoletas)

print(f"Archivo CSV '{filename}' exportado exitosamente.")

#Importacion de una sola guia - Verificar cuantas hay de dos guias