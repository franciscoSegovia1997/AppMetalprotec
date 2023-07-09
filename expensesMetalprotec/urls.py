from django.urls import path, include
from . import views

app_name='expensesMetalprotec'

urlpatterns = [
    path('boxRegister',views.boxRegister,name='boxRegister'),
    path('costRegister',views.costRegister,name='costRegister'),
    path('datacenter',views.datacenter,name='datacenter'),
    path('purchaseOrder',views.purchaseOrder,name='purchaseOrder'),
    path('deleteDivision/<str:idDivision>',views.deleteDivision,name='deleteDivision'),
    path('deleteCategory/<str:idCategory>',views.deleteCategory,name='deleteCategory'),
    path('deleteDeparment/<str:idDeparment>',views.deleteDeparment,name='deleteDeparment'),
    path('newDeparment',views.newDeparment,name='newDeparment'),
    path('newCategory',views.newCategory,name='newCategory'),
    path('getCategories',views.getCategories,name='getCategories'),
    path('newDivision',views.newDivision,name='newDivision'),
]
