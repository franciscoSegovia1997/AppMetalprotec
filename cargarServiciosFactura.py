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
from salesMetalprotec.models import quotationSystem, guideSystem, billSystem

billSystem.objects.all().delete()

filename = 'cargaMetalprotec/facturasServiciosMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointBill = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
            
        origenFactura = 'QUIOTATION'
        asociatedQuotation = quotationSystem.objects.get(codeQuotation=row[10])

        itemFactura = 'SERVICIOS'

        infoFactura = billSystem.objects.create(
            endpointBill=endpointBill,
            commentBill=row[0],
            dateBill=datetime.datetime.strptime(row[1],'%Y-%m-%d'),
            relatedDocumentBill=row[2],
            erBuy=row[3],
            erSel=row[4],
            currencyBill=row[5],
            stateBill=row[6],
            codeBill=row[7],
            stateTeFacturo=row[8],
            nroBill=row[9],
            typeItemsBill=itemFactura,
            originBill=origenFactura,
            asociatedQuotation=asociatedQuotation
        )

print('Carga finalizada exitosamente')