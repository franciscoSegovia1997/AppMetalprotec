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
    path('editDataQuotation/<str:idQuotation>',views.editDataQuotation,name='editDataQuotation'),
    path('editDataGuide/<str:idGuide>',views.editDataGuide,name='editDataGuide'),
    path('editDataBill/<str:idBill>',views.editDataBill,name='editDataBill'),
    path('editDataInvoice/<str:idInvoice>',views.editDataInvoice,name='editDataInvoice'),
    path('updateQuotation',views.updateQuotation,name='updateQuotation'),
    path('updateGuide',views.updateGuide,name='updateGuide'),
    path('updateBill',views.updateBill,name='updateBill'),
    path('updateInvoice',views.updateInvoice,name='updateInvoice'),
    path('createGuideFromQuotation/<str:idQuotation>',views.createGuideFromQuotation,name='createGuideFromQuotation'),
    path('createBillFromGuide/<str:idGuide>',views.createBillFromGuide,name='createBillFromGuide'),
    path('createInvoiceFromGuide/<str:idGuide>',views.createInvoiceFromGuide,name='createInvoiceFromGuide'),
    path('createBillFromQuotation/<str:idQuotation>', views.createBillFromQuotation,name='createBillFromQuotation'),
    path('createInvoiceFromQuotation/<str:idQuotation>', views.createInvoiceFromQuotation,name='createInvoiceFromQuotation'),
    path('cancelQuotation/<str:idQuotation>',views.cancelQuotation,name='cancelQuotation'),
    path('downloadQuotationDolares/<str:idQuotation>',views.downloadQuotationDolares,name='downloadQuotationDolares'),
    path('downloadQuotationSoles/<str:idQuotation>',views.downloadQuotationSoles,name='downloadQuotationSoles'),
    path('sendGuideTeFacturo/<str:idGuide>',views.sendGuideTeFacturo,name='sendGuideTeFacturo'),
    path('verifyGuideTeFacturo/<str:idGuide>',views.verifyGuideTeFacturo,name='verifyGuideTeFacturo'),
    path('downloadGuideTeFacturo/<str:idGuide>',views.downloadGuideTeFacturo,name='downloadGuideTeFacturo'),
]