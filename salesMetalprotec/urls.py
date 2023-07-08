from django.urls import path, include
from . import views

app_name='salesMetalprotec'

urlpatterns = [
    path('quotationsMetalprotec',views.quotationsMetalprotec,name='quotationsMetalprotec'),
    path('guidesMetalprotec',views.guidesMetalprotec,name='guidesMetalprotec'),
    path('billsMetalprotec',views.billsMetalprotec,name='billsMetalprotec'),
    path('invoicesMetalprotec',views.invoicesMetalprotec,name='invoicesMetalprotec'),
    path('creditNotesMetalprotec',views.creditNotesMetalprotec,name='creditNotesMetalprotec'),
    path('newQuotation',views.newQuotation,name='newQuotation')
]