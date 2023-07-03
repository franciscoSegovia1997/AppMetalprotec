from django.urls import path, include
from . import views

app_name='usersMetalprotec'

urlpatterns = [
    path('',views.loginSystem,name='loginSystem'),
    path('usuarios',views.usersMetalprotec,name='usersMetalprotec'),
]
