import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser
from clientsMetalprotec.models import clientSystem
from financeMetalprotec.models import bankSystem
from financeMetalprotec.models import paymentSystem
from salesMetalprotec.models import invoiceSystem, billSystem
import datetime

filename = 'cargaMetalprotec/abonosActuales.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointPayment = usuarioRaiz.extendeduser.endpointUser

paymentSystem.objects.all().delete()

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:

        asociatedBank=bankSystem.objects.filter(nameBank=row[7]).filter(currencyBank=row[8])[0]

        if row[9] == 'BILL':
            asociatedBill = billSystem.objects.filter(codeBill=row[1])[0]
            asociatedBill.paidBill = '1'
            asociatedBill.save()
            asociatedInvoice = None
        else:
            asociatedInvoice = invoiceSystem.objects.filter(codeInvoice=row[1])[0]
            asociatedInvoice.paidInvoice = '1'
            asociatedInvoice.save()
            asociatedBill = None
        paymentSystem.objects.create(
           datePayment=datetime.datetime.strptime(row[0],'%Y-%m-%d'),
           nameBankPayment=row[7],
           currencyPayment=row[8],
           operationNumber=row[10],
           operationNumber2=row[11],
           nameClient=row[12],
           statePayment=row[6],
           codeDocument=row[1],
           codeGuide=row[2],
           codeQuotation=row[3],
           codeSeller=row[4],
           typeDocumentPayment=row[9],
           enabledComission=row[5],
           asociatedBank=asociatedBank,
           asociatedBill=asociatedBill,
           asociatedInvoice=asociatedInvoice,
           endpointPayment=endpointPayment
        )

print('Carga finalizada exitosamente')