import os
import django
import csv

# Configura la variable de entorno para el módulo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AppMetalprotec.settings")

# Inicializa Django
django.setup()

from django.contrib.auth.models import User
from usersMetalprotec.models import extendedUser

filename = 'cargaMetalprotec/usuariosMetalprotec.csv'

with open(filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        username=row[0]
        first_name=row[1]
        last_name=row[2]
        email=row[3]
        codeUser=row[4]
        phoneUser=row[6]
        nuevoUsuario = User.objects.create(
            username=username,
            email=email
        )
        nuevoUsuario.set_password(username)
        nuevoUsuario.first_name=first_name
        nuevoUsuario.last_name=last_name
        nuevoUsuario.is_staff=True
        nuevoUsuario.save()
        extendedUser.objects.create(
            asociatedUser=nuevoUsuario,
            codeUser=codeUser,
            nameUser=first_name,
            lastnameUser=last_name,
            phoneUser=phoneUser
        )

print('Carga finalizada exitosamente')