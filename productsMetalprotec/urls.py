from django.urls import path, include
from . import views

app_name='productsMetalprotec'

urlpatterns = [
    path('',views.productsMetalprotec,name='productsMetalprotec'),
]
