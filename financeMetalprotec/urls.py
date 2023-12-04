from django.urls import path, include
from . import views

app_name='financeMetalprotec'

urlpatterns = [
    path('bankRegisters',views.bankRegisters,name='bankRegisters'),
    path('comissions',views.comissions,name='comissions'),
    path('paymentsRegister',views.paymentsRegister,name='paymentsRegister'),
    path('deleteBankRegister/<str:idBank>',views.deleteBankRegister,name='deleteBankRegister'),
    path('getDocuments',views.getDocuments,name='getDocuments'),
    path('deletePayment/<str:idPayment>',views.deletePayment,name='deletePayment'),
    path('updatePayment',views.updatePayment,name='updatePayment'),
    path('getPaymentData',views.getPaymentData,name='getPaymentData'),
    path('getRelatedDocuments',views.getRelatedDocuments,name='getRelatedDocuments'),
    path('settingsComissions',views.settingsComissions,name='settingsComissions'),
    path('deleteSettingComssion/<str:idComission>',views.deleteSettingComssion,name='deleteSettingComssion'),
    path('getConfigComission',views.getConfigComission,name='getConfigComission'),
    path('getComissionData',views.getComissionData,name='getComissionData'),
    path('exportComissions',views.exportComissions,name='exportComissions'),
    path('showBankRegister/<str:idBankRegister>',views.showBankRegister,name='showBankRegister'),
    path('downloadAllPayments',views.downloadAllPayments,name='downloadAllPayments'),
]