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
from salesMetalprotec.models import invoiceSystem,guideSystem
import datetime

filename = 'boletasMetalprotec.csv'

invoiceSystem.objects.all().delete()

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointInvoice = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        try:
            infoBoleta = invoiceSystem.objects.create(
                commentInvoice=row[0],
                dateInvoice=datetime.datetime.strptime(row[1],'%Y-%m-%d'),
                relatedDocumentInvoice=row[2],
                erBuy=row[3],
                erSel=row[4],
                currencyInvoice=row[5],
                stateInvoice=row[6],
                codeInvoice=row[7],
                stateTeFacturo=row[8],
                nroInvoice=row[9],
                typeItemsInvoice=row[10],
                originInvoice=row[11],
                endpointInvoice=endpointInvoice
            )
            guideObject = guideSystem.objects.get(codeGuide=row[12])
            guideObject.asociatedInvoice = infoBoleta
            guideObject.save()
        except:
            pass

print('Carga finalizada exitosamente')