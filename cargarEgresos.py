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
from salesMetalprotec.models import invoiceSystem,guideSystem,creditNoteSystem, billSystem, invoiceSystem
from stockManagment.models import incomingItemsRegisterInfo, outcomingItemsRegisterInfo
import datetime
from productsMetalprotec.models import productSystem, storeSystem

filename = 'cargaMetalprotec/egresosMetalprotec.csv'

outcomingItemsRegisterInfo.objects.all().delete()

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointOutcoming = usuarioRaiz.extendeduser.endpointUser

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

        if row[8][0] == 'E':
            asociatedBill=None
            asociatedInvoice=None
        else:
            if row[8][0] == 'F':
                try:
                    asociatedBill = billSystem.objects.get(codeCreditNote=row[8])
                    asociatedInvoice = None
                except:
                    asociatedBill=None
                    asociatedInvoice = None
            else:
                try:
                    asociatedBill = None
                    asociatedInvoice = invoiceSystem.objects.get(codeCreditNote=row[8])
                except:
                    asociatedBill=None
                    asociatedInvoice = None
        try:
            asociatedStore = storeSystem.objects.get(nameStore=row[3].upper())
        except:
            asociatedStore = None

        outcomingItemsRegisterInfo.objects.create(
            dateOutcoming = datetime.datetime.strptime(row[0],'%Y-%m-%d'),
            productCode=row[1],
            nameStore=row[3].upper(),
            quantityProduct=row[4],
            lastStock=row[5],
            newStock=row[6],
            typeOutcoming=row[7],
            referenceOutcome=row[8],
            asociatedUserData=asociatedUser,
            asociatedProduct=asociatedProduct,
            asociatedBill=asociatedBill,
            asociatedInvoice=asociatedInvoice,
            asociatedStoreData=asociatedStore,
            endpointOutcoming=endpointOutcoming
        )

print('Carga finalizada exitosamente')