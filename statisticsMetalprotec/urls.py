from django.urls import path
from . import views

app_name='statisticsMetalprotec'

urlpatterns = [
    path('mainDashboard',views.mainDashboard,name='mainDashboard'),
    path('clientsDashboard',views.clientsDashboard,name='clientsDashboard'),
    path('productsDashboard',views.productsDashboard,name='productsDashboard'),
    path('sellDashboard',views.sellDashboard,name='sellDashboard'),
    path('productsStatistics',views.productsStatistics,name='productsStatistics'),
    path('clientStatistics',views.clientStatistics,name='clientStatistics'),
    path('sellerStatistics',views.sellerStatistics,name='sellerStatistics'),
    path('resumeSalesxYear',views.resumeSalesxYear,name='resumeSalesxYear'),
    path('salesxMonths',views.salesxMonths,name='salesxMonths'),
    path('sellerSalesTime',views.sellerSalesTime,name='sellerSalesTime'),
]
