import os
import django
import csv
from django.db.models import Q
import datetime

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from salesMetalprotec.models import billSystem
from salesMetalprotec.models import invoiceSystem
from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser

print("Job de homologacion de facturas y boletas")

billFilter = billSystem.objects.filter(
    Q(dateBill__gte=datetime.datetime.strptime('2023-08-01','%Y-%m-%d').date()) &
    Q(dateBill__lte=datetime.datetime.strptime('2023-08-31','%Y-%m-%d').date())
).exclude(stateTeFacturo=None).exclude(stateTeFacturo='Anulada').exclude(stateTeFacturo='').exclude(stateTeFacturo='Rechazado')

invoiceFilter = invoiceSystem.objects.filter(
    Q(dateInvoice__gte=datetime.datetime.strptime('2023-08-01','%Y-%m-%d').date()) &
    Q(dateInvoice__lte=datetime.datetime.strptime('2023-08-31','%Y-%m-%d').date())
).exclude(stateTeFacturo=None).exclude(stateTeFacturo='Anulada').exclude(stateTeFacturo='').exclude(stateTeFacturo='Rechazado')

print(f"Se homologaran {len(billFilter)} facturas y {len(invoiceFilter)} boletas")

print("Hologando las facturas")
for billItem in billFilter:
    currencyBill = billItem.currencyBill
    if billItem.originBill == 'GUIDE':
        for guideItem in billItem.guidesystem_set.all():
            quotationItem = guideItem.asociatedQuotation
            quotationItem.currencyQuotation = currencyBill
            quotationItem.save()
    else:
        quotationItem = billItem.asociatedQuotation
        quotationItem.currencyQuotation = currencyBill
        quotationItem.save()
    print(f"Factura {billItem.codeBill}, Coti {quotationItem.codeQuotation} homologada: FACTURA: {billItem.currencyBill} - COTIZACION: {quotationItem.currencyQuotation}")

print("Homologando las boletas")
for invoiceItem in invoiceFilter:
    currencyInvoice = invoiceItem.currencyInvoice
    if invoiceItem.originInvoice == 'GUIDE':
        for guideItem in invoiceItem.guidesystem_set.all():
            quotationItem = guideItem.asociatedQuotation
            quotationItem.currencyQuotation = currencyInvoice
            quotationItem.save()
    else:
        quotationItem = invoiceItem.asociatedQuotation
        quotationItem.currencyQuotation = currencyInvoice
        quotationItem.save()
    print(f"Boleta {invoiceItem.codeInvoice} homologada: BOLETA: {invoiceItem.currencyInvoice} - COTIZACION: {quotationItem.currencyQuotation}")