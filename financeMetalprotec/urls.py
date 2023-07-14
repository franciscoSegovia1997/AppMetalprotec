from django.urls import path, include
from . import views

app_name='financeMetalprotec'

urlpatterns = [
    path('bankRegisters',views.bankRegisters,name='bankRegisters'),
    path('comissions',views.comissions,name='comissions'),
    path('paymentsRegister',views.paymentsRegister,name='paymentsRegister'),
    path('deleteBankRegister/<str:idBank>',views.deleteBankRegister,name='deleteBankRegister')
]