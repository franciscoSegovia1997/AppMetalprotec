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
from salesMetalprotec.models import quotationSystem, quotationClientData,quotationSellerData,quotationProductData, quotationServiceData
from clientsMetalprotec.models import clientSystem
from productsMetalprotec.models import productSystem
from servicesMetalprotec.models import serviceSystem

quotationServiceData.objects.all().delete()

filename = 'cargaMetalprotec/serviciosCotizaciones.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointQuotation = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        asociatedQuotation =quotationSystem.objects.get(codeQuotation=row[0])
        infoService = row
        del infoService[0]
        try:
            asociatedService = serviceSystem.objects.get(nameService=infoService[1])
            infoService[0] = str(asociatedService.id)

            quotationServiceData.objects.create(
                asociatedQuotation=asociatedQuotation,
                asociatedService=asociatedService,
                dataServiceQuotation=infoService
            )
        except:
            infoService[0] = '0'

            quotationServiceData.objects.create(
                asociatedQuotation=asociatedQuotation,
                dataServiceQuotation=infoService
            )
            print(infoService)