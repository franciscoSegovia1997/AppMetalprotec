from django.urls import path, include
from . import views

app_name='productsMetalprotec'

urlpatterns = [
    path('',views.productsMetalprotec,name='productsMetalprotec'),
    path('deleteProduct',views.deleteProduct,name='deleteProduct'),
    path('getProductData',views.getProductData,name='getProductData'),
    path('updateProduct',views.updateProduct,name='updateProduct'),
    path('getProductStock',views.getProductStock,name='getProductStock'),
    path('addStockProduct',views.addStockProduct,name='addStockProduct'),
]