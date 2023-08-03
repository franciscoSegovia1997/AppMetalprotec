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
from salesMetalprotec.models import invoiceSystem,billSystem,guideSystem, creditNoteSystem
import datetime

filename = 'notasMetalprotec.csv'

creditNoteSystem.objects.all().delete()

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointCreditNote = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if row[0] == 'NONE':
            creditNoteSystem.objects.create(
                typeCreditNote=row[1],
                stateCreditNote=row[2],
                codeCreditNote=row[3],
                stateTeFacturo=row[4],
                dateCreditNote=datetime.datetime.strptime(row[5],'%Y-%m-%d'),
                nroCreditNote=row[6],
                originCreditNote=row[7],
                endpointCreditNote=endpointCreditNote
            )
        else:
            if row[7] == 'INVOICE':
                invoiceObject = invoiceSystem.objects.get(codeInvoice=row[0])
                creditNoteSystem.objects.create(
                    asociatedInvoice=invoiceObject,
                    typeCreditNote=row[1],
                    stateCreditNote=row[2],
                    codeCreditNote=row[3],
                    stateTeFacturo=row[4],
                    dateCreditNote=datetime.datetime.strptime(row[5],'%Y-%m-%d'),
                    nroCreditNote=row[6],
                    originCreditNote=row[7],
                    endpointCreditNote=endpointCreditNote
                )
            else:
                try:
                    billObject = billSystem.objects.get(codeBill=row[0])
                    creditNoteSystem.objects.create(
                        asociatedBill=billObject,
                        typeCreditNote=row[1],
                        stateCreditNote=row[2],
                        codeCreditNote=row[3],
                        stateTeFacturo=row[4],
                        dateCreditNote=datetime.datetime.strptime(row[5],'%Y-%m-%d'),
                        nroCreditNote=row[6],
                        originCreditNote=row[7],
                        endpointCreditNote=endpointCreditNote
                    )
                except:
                    creditNoteSystem.objects.create(
                        typeCreditNote=row[1],
                        stateCreditNote=row[2],
                        codeCreditNote=row[3],
                        stateTeFacturo=row[4],
                        dateCreditNote=datetime.datetime.strptime(row[5],'%Y-%m-%d'),
                        nroCreditNote=row[6],
                        originCreditNote=row[7],
                        endpointCreditNote=endpointCreditNote
                    )

print('Carga finalizada exitosamente')