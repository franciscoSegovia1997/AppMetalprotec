from django.urls import path, include
from . import views

app_name='settingsMetalprotec'

urlpatterns = [
    path('',views.settingsMetalprotec,name='settingsMetalprotec'),
    path('deleteEndpoint',views.deleteEndpoint,name='deleteEndpoint'),
    path('getEndpointData',views.getEndpointData,name='getEndpointData'),
    path('updateEndpoint',views.updateEndpoint,name='updateEndpoint'),
]
