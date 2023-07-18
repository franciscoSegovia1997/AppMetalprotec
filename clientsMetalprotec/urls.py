from django.urls import path, include
from . import views

app_name='clientsMetalprotec'

urlpatterns = [
    path('',views.clientsMetalprotec,name='clientsMetalprotec'),
    path('deleteClient',views.deleteClient,name='deleteClient'),
    path('getClientData',views.getClientData,name='getClientData'),
    path('updateClient',views.updateClient,name='updateClient'),
    path('getClientAddress',views.getClientAddress,name='getClientAddress'),
    path('addClientAddress',views.addClientAddress,name='addClientAddress'),
    path('importClientsData',views.importClientsData,name='importClientsData')
]
