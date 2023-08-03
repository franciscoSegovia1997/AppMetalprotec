import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from salesMetalprotec.models import invoiceSystem, creditNoteSystem

notasTotales = creditNoteSystem.objects.all()

arregloNotas = []
for notaInfo in notasTotales:
    if notaInfo.typeCreditNote == 'INVOICE':
        datosNota = [
            notaInfo.asociatedInvoice.codeInvoice,
            notaInfo.typeCreditNote,
            notaInfo.stateCreditNote,
            notaInfo.codeCreditNote,
            notaInfo.stateTeFacturo,
            notaInfo.dateCreditNote,
            notaInfo.nroCreditNote,
            notaInfo.originCreditNote
        ]
    else:
        try:
            datosNota = [
                notaInfo.asociatedBill.codeBill,
                notaInfo.typeCreditNote,
                notaInfo.stateCreditNote,
                notaInfo.codeCreditNote,
                notaInfo.stateTeFacturo,
                notaInfo.dateCreditNote,
                notaInfo.nroCreditNote,
                notaInfo.originCreditNote
            ]
        except:
            datosNota = [
                'NONE',
                notaInfo.typeCreditNote,
                notaInfo.stateCreditNote,
                notaInfo.codeCreditNote,
                notaInfo.stateTeFacturo,
                notaInfo.dateCreditNote,
                notaInfo.nroCreditNote,
                notaInfo.originCreditNote
            ]
    
    arregloNotas.append(datosNota)

filename = 'notasMetalprotec.csv'

with open(filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(arregloNotas)

print(f"Archivo CSV '{filename}' exportado exitosamente.")

#Importacion de una sola guia - Verificar cuantas hay de dos guias