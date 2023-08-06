from django.urls import path
from . import views

app_name='stockManagment'

urlpatterns = [
    path('incomingItems',views.incomingItems,name='incomingItems'),
    path('outcomingItems',views.outcomingItems,name='outcomingItems'),
    path('stockTaking',views.stockTaking,name='stockTaking'),
    path('deleteStockTaking/<str:idStockTaking>',views.deleteStockTaking,name='deleteStockTaking'),
    path('downloadStockTaking/<str:idStockTaking>',views.downloadStockTaking,name='downloadStockTaking'),
    path('exportFilteredIncomingItems',views.exportFilteredIncomingItems,name='exportFilteredIncomingItems'),
    path('filterIncomingItemsJson',views.filterIncomingItemsJson,name='filterIncomingItemsJson'),
]