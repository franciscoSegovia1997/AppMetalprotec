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
from salesMetalprotec.models import quotationSystem

quotationSystem.objects.all().delete()

filename = 'cargaMetalprotec/cotizacionesMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointQuotation = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if row[16] == '1':
            showDiscount = 'ON'
        else:
            showDiscount = 'OFF'

        if row[15] == '1':
            showUnitPrice= 'ON'
        else:
            showUnitPrice = 'OFF'

        if row[14] == '1':
            showSellPrice = 'ON'
        else:
            showSellPrice = 'OFF'
        

        quotationSystem.objects.create(
            showDiscount = showDiscount,
            showUnitPrice = showUnitPrice,
            showSellPrice = showSellPrice,
            relatedDocumentQuotation = row[13],
            commentQuotation = row[12],
            quotesQuotation = row[11],
            expirationCredit = row[10],
            expirationQuotation = row[9],
            numberQuotation = row[8],
            erBuy = row[6],
            erSel = row[7],
            codeQuotation = row[0],
            stateQuotation = row[5].upper(),
            paymentQuotation = row[4],
            dateQuotation = datetime.datetime.strptime(row[2],'%Y-%m-%d'),
            typeQuotation = row[1].upper(),
            currencyQuotation = row[3],
            endpointQuotation=endpointQuotation
        )

print('Carga finalizada exitosamente')