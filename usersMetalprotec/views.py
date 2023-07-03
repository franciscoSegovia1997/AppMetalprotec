from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import rolesxUser, extendedUser

# Create your views here.
def loginSystem(request):
    if request.method == 'POST':
        userUsername = request.POST.get('userUsername')
        userPassword = request.POST.get('userPassword')
        userSystem = authenticate(request,username=userUsername,password=userPassword)
        if userSystem is not None:
            login(request,userSystem)
            return HttpResponseRedirect(reverse('usersMetalprotec:welcomeMetalprotec'))
        else:
            return HttpResponseRedirect(reverse('usersMetalprotec:loginSystem'))
    return render(request,'loginSystem.html')

@login_required(login_url='/')
def welcomeMetalprotec(request):
    return render(request,'welcomeMetalprotec.html')

@login_required(login_url='/')
def usersMetalprotec(request):
    if request.method=='POST':
        newUsername = request.POST.get('newUsername')
        newPassword = request.POST.get('newPassword')
        newName = request.POST.get('newName')
        newLastName = request.POST.get('newLastName')
        newEmail = request.POST.get('newEmail')
        newPhone = request.POST.get('newPhone')
        newRole = request.POST.get('newRole')

        if checkUsernameExist(newUsername):
            return HttpResponseRedirect(reverse('usersMetalprotec:usersMetalprotec'))
        else:
            newUserObject = User.objects.create(
                username=newUsername,
                email=newEmail
            )

            newUserObject.set_password(newPassword)
            newUserObject.first_name = newName
            newUserObject.last_name = newLastName
            newUserObject.is_staff = True
            newUserObject.save()

            newCodeUser = str(newUserObject.id)
            while len(newCodeUser) < 4:
                newCodeUser = '0' + newCodeUser
            newCodeUser = 'USR-' + newCodeUser

            roleUserObject = rolesxUser.objects.get(nameRole=newRole)

            extendedUser.objects.create(
                asociatedUser=newUserObject,
                codeUser=newCodeUser,
                nameUser=newName,
                lastnameUser=newLastName,
                phoneUser=newPhone,
                roleUser=roleUserObject,
            )
            return HttpResponseRedirect(reverse('usersMetalprotec:usersMetalprotec'))
    return render(request,'usersMetalprotec.html',{
        'usersSystem':User.objects.all().order_by('id'),
        'rolesSystem':rolesxUser.objects.all().order_by('id'),
    })

def checkUsernameExist(username):
    try:
        userCheck = User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False

@login_required(login_url='/')
def deleteUser(request,idUser):
    userData = User.objects.get(id=idUser)
    userData.delete()
    return HttpResponseRedirect(reverse('usersMetalprotec:usersMetalprotec'))

@login_required(login_url='/')
def updateUser(request):
    return HttpResponseRedirect(reverse('usersMetalprotec:usersMetalprotec'))

@login_required(login_url='/')
def logoutSystem(request):
    logout(request)
    return HttpResponseRedirect(reverse('usersMetalprotec:loginSystem'))
