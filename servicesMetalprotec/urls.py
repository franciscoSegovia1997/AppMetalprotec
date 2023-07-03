from django.urls import path, include
from . import views

app_name='servicesMetalprotec'

urlpatterns = [
    path('',views.servicesMetalprotec,name='servicesMetalprotec'),
]
