from django.urls import path, include
from . import views

app_name='salesMetalprotec'

urlpatterns = [
    path('quotationsMetalprotec',views.quotationsMetalprotec,name='quotationsMetalprotec'),
    path('guidesMetalprotec',views.guidesMetalprotec,name='guidesMetalprotec'),
    path('billsMetalprotec',views.billsMetalprotec,name='billsMetalprotec'),
    path('invoicesMetalprotec',views.invoicesMetalprotec,name='invoicesMetalprotec'),
    path('creditNotesMetalprotec',views.creditNotesMetalprotec,name='creditNotesMetalprotec'),
    path('newQuotation',views.newQuotation,name='newQuotation'),
    path('createGuideFromQuotation/<str:idQuotation>',views.createGuideFromQuotation,name='createGuideFromQuotation'),
    path('editDataGuide/<str:idGuide>',views.editDataGuide,name='editDataGuide'),
    path('updateGuide',views.updateGuide,name='updateGuide'),
    path('updateBill',views.updateBill,name='updateBill'),
    path('updateInvoice',views.updateInvoice,name='updateInvoice'),
    path('createBillFromGuide/<str:idGuide>',views.createBillFromGuide,name='createBillFromGuide'),
    path('editDataBill/<str:idBill>',views.editDataBill,name='editDataBill'),
]