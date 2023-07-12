from django.urls import path
from . import views

app_name='stockManagment'

urlpatterns = [
    path('incomingItems',views.incomingItems,name='incomingItems'),
    path('outcomingItems',views.outcomingItems,name='outcomingItems'),
    path('stockTaking',views.stockTaking,name='stockTaking'),
]