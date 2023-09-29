from django.urls import path, include
from . import views

app_name='usersMetalprotec'

urlpatterns = [
    path('',views.loginSystem,name='loginSystem'),
    path('usersMetalprotec',views.usersMetalprotec,name='usersMetalprotec'),
    path('welcomeMetalprotec',views.welcomeMetalprotec,name='welcomeMetalprotec'),
    path('logoutSystem',views.logoutSystem,name='logoutSystem'),
    path('deleteUser',views.deleteUser,name='deleteUser'),
    path('updateUser',views.updateUser,name='updateUser'),
    path('getUserData',views.getUserData,name='getUserData'),
    path('usersMetalprotec/getDataOne',views.getDataOne,name='getDataOne'),
    path('usersMetalprotec/getDataAll',views.getDataAll,name='getDataAll'),
    path('assignRoleUser',views.assignRoleUser,name='assignRoleUser'),
    path('assignEndpointUser',views.assignEndpointUser,name='assignEndpointUser'),
]
