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
from salesMetalprotec.models import billSystem
from productsMetalprotec.models import productSystem,storexproductSystem
from salesMetalprotec.models import quotationSystem, quotationProductData

storeProduct = storexproductSystem.objects.filter(asociatedProduct__codeProduct='2392999903').get(asociatedStore__nameStore='TRUJILLO')
p1 = storeProduct.asociatedProduct

print(p1.codeProduct)
print(p1.nameProduct)

allQuotation = quotationProductData.objects.filter(dataProductQuotation__2=p1.codeProduct)
print(f"La cantidad de registros es : {len(allQuotation)}")
quotationInfo = allQuotation.filter(asociatedQuotation__stateQuotation='EMITIDA').filter(
    asociatedQuotation__dateQuotation__year__gte=2023,
    asociatedQuotation__dateQuotation__month__gte=6
)
print(f"La cantidad de cotizaciones es : {len(quotationInfo)}")
for quotationData in quotationInfo:
    print(quotationData.asociatedQuotation.guidesystem.asociatedBill.codeBill)
