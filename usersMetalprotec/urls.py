from django.urls import path, include
from . import views

app_name='usersMetalprotec'

urlpatterns = [
    path('',views.loginSystem,name='loginSystem'),
    path('usersMetalprotec',views.usersMetalprotec,name='usersMetalprotec'),
    path('welcomeMetalprotec',views.welcomeMetalprotec,name='welcomeMetalprotec'),
    path('logoutSystem',views.logoutSystem,name='logoutSystem'),
    path('deleteUser/<str:idUser>',views.deleteUser,name='deleteUser'),
    path('updateUser',views.updateUser,name='updateUser'),
]
