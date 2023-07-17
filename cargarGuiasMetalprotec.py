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
from salesMetalprotec.models import quotationSystem, guideSystem

guideSystem.objects.all().delete()

filename = 'cargaMetalprotec/guiasMetalprotec.csv'

usuarioRaiz = User.objects.get(username='adminMetalprotec2023')
endpointGuide = usuarioRaiz.extendeduser.endpointUser

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row[0])
        asociatedQuotation = quotationSystem.objects.get(codeQuotation=row[0])
        guideSystem.objects.create(
            endpointGuide=endpointGuide,
            asociatedQuotation=asociatedQuotation,
            commentGuide=row[1],
            dateGuide=datetime.datetime.strptime(row[2],'%Y-%m-%d'),
            dateGivenGoods=datetime.datetime.strptime(row[2],'%Y-%m-%d'),
            purposeTransportation=row[3],
            modeTransportation=row[4],
            extraWeight=row[5],
            ubigeoClient=row[6],
            deparmentDeparture=row[7],
            provinceDeparture=row[8],
            districtDeparture=row[9],
            addressDeparture=row[10],
            ubigeoDeparture=row[11],
            razonSocialTranporter=row[12],
            rucTransporter=row[13],
            vehiclePlate=row[14],
            dniDriver=row[15],
            licenceDriver=row[16],
            nameDriver=row[17],
            stateGuide=row[18].upper(),
            codeGuide=row[19],
            stateTeFacturo=row[20],
            nroGuide=row[21]
        )

print('Carga finalizada exitosamente')


#Arreglar la guia 398 en produccion, en desarrollo y test no hay problem
#Se Elimino la guia 450, averiguar como recuperarla
#verficar la 422 tambien
#VERIFICAR 417
#VERIFICAR 401
#VERIFICAR 397
#VERIFICAR 389
#VERIFICAR 386
#VERIFICAR 380
#VERIFICAR 317
#VERIFICAR 363
#EVRIFICAR 354
#VERIFICAR 353
#VERIFICAR 342
#VERIFICAR 336
#VERIFICAR 333
#VERIFICAR 331
#VERIFICAR 323