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
from salesMetalprotec.models import invoiceSystem,guideSystem,creditNoteSystem
from stockManagment.models import incomingItemsRegisterInfo
import datetime
from productsMetalprotec.models import productSystem, storeSystem

filename = 'cargaMetalprotec/ingresosMetalprotec.csv'

incomingItemsRegisterInfo.objects.all().delete()

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointIncoming = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        try:
            asociatedUser = extendedUser.objects.get(codeUser=row[9]).asociatedUser
        except:
            asociatedUser = None
        try:
            asociatedProduct = productSystem.objects.get(codeProduct=row[1])
        except:
            asociatedProduct = None

        if row[8] == 'Ingreso productos':
            asociatedCreditNote=None
        else:
            try:
                asociatedCreditNote = creditNoteSystem.objects.get(codeCreditNote=row[8])
            except:
                asociatedCreditNote=None
        try:
            asociatedStore = storeSystem.objects.get(nameStore=row[3].upper())
        except:
            asociatedStore = None

        incomingItemsRegisterInfo.objects.create(
            dateIncoming = datetime.datetime.strptime(row[0],'%Y-%m-%d'),
            productCode=row[1],
            nameStore=row[3].upper(),
            quantityProduct=row[4],
            lastStock=row[5],
            newStock=row[6],
            typeIncoming=row[7],
            referenceIncome=row[8],
            asociatedUserData=asociatedUser,
            asociatedProduct=asociatedProduct,
            asociatedCreditNote=asociatedCreditNote,
            asociatedStoreData=asociatedStore,
            endpointIncoming=endpointIncoming
        )

print('Carga finalizada exitosamente')