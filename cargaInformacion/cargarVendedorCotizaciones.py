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
from salesMetalprotec.models import quotationSystem, quotationClientData,quotationSellerData
from clientsMetalprotec.models import clientSystem

quotationSellerData.objects.all().delete()

filename = 'cargaMetalprotec/usuariosCotizaciones.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointQuotation = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        asociatedQuotation =quotationSystem.objects.get(codeQuotation=row[0])
        infoUser = row
        del infoUser[0]

        asociatedUser = extendedUser.objects.get(codeUser=infoUser[2]).asociatedUser
        infoUser[0] = str(asociatedUser.id)

        quotationSellerData.objects.create(
            asociatedQuotation=asociatedQuotation,
            asociatedUser=asociatedUser,
            dataUserQuotation=infoUser
        )
