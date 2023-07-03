from django.urls import path, include
from . import views

app_name='clientsMetalprotec'

urlpatterns = [
    path('',views.clientsMetalprotec,name='clientsMetalprotec'),
]
