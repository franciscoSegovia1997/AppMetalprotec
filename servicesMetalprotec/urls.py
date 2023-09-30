from django.urls import path, include
from . import views

app_name='servicesMetalprotec'

urlpatterns = [
    path('',views.servicesMetalprotec,name='servicesMetalprotec'),
    path('deleteService',views.deleteService,name='deleteService'),
    path('getServiceData',views.getServiceData,name='getServiceData'),
    path('updateService',views.updateService,name='updateService'),
    path('getDataOne',views.getDataOne,name='getDataOne'),
    path('getDataAll',views.getDataAll,name='getDataAll')
]
