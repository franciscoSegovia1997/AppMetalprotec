from django.urls import path, include
from . import views

app_name='expensesMetalprotec'

urlpatterns = [
    path('boxRegisterFunction',views.boxRegisterFunction,name='boxRegisterFunction'),
    path('costRegisterFunction',views.costRegisterFunction,name='costRegisterFunction'),
    path('datacenter',views.datacenter,name='datacenter'),
    path('purchaseOrder',views.purchaseOrder,name='purchaseOrder'),
    path('deleteDivision/<str:idDivision>',views.deleteDivision,name='deleteDivision'),
    path('deleteCategory/<str:idCategory>',views.deleteCategory,name='deleteCategory'),
    path('deleteDeparment/<str:idDeparment>',views.deleteDeparment,name='deleteDeparment'),
    path('newDeparment',views.newDeparment,name='newDeparment'),
    path('newCategory',views.newCategory,name='newCategory'),
    path('getCategories',views.getCategories,name='getCategories'),
    path('newDivision',views.newDivision,name='newDivision'),
    path('getDivisionData',views.getDivisionData,name='getDivisionData'),
    path('deleteCostRegister/<str:idRegister>',views.deleteCostRegister,name='deleteCostRegister'),
    path('getDataRegisterInfo',views.getDataRegisterInfo,name='getDataRegisterInfo'),
    path('deleteBoxRegister/<str:idBoxRegister>',views.deleteBoxRegister,name='deleteBoxRegister'),
    path('showBoxInfo/<str:idBoxRegister>',views.showBoxInfo,name='showBoxInfo'),
    path('deleteCashIncome/<str:idCashIncome>&<str:idBoxRegister>',views.deleteCashIncome,name='deleteCashIncome'),
    path('createIncomeBox/<str:idBoxInfo>',views.createIncomeBox,name='createIncomeBox'),
    path('newPurchaseOrder',views.newPurchaseOrder,name='newPurchaseOrder'),
    path('getProductInfoExpenses/<str:ind>',views.getProductInfoExpenses,name='getProductInfoExpenses'),
    path('createOrden', views.createOrden, name='createOrden'),
    path('deleteOrden/<str:ind>',views.deleteOrden,name='deleteOrden'),
    path('downloadOrden/<str:ind>',views.downloadOrden,name='downloadOrden')
]
