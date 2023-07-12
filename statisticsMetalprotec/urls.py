from django.urls import path
from . import views

app_name='statisticsMetalprotec'

urlpatterns = [
    path('mainDashboard',views.mainDashboard,name='mainDashboard'),
    path('clientsDashboard',views.clientsDashboard,name='clientsDashboard'),
    path('productsDashboard',views.productsDashboard,name='productsDashboard'),
    path('sellDashboard',views.sellDashboard,name='sellDashboard'),
]
