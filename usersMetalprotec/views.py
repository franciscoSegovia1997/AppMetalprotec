from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
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
def deleteUser(request):
    if request.method == 'POST':
        deleteIdUser = request.POST.get('deleteIdUser')
        deleteUser = User.objects.get(id=deleteIdUser)
        deleteUser.delete()
        return HttpResponseRedirect(reverse('usersMetalprotec:usersMetalprotec'))

@login_required(login_url='/')
def updateUser(request):
    if request.method == 'POST':
        editIdUser = request.POST.get('editIdUser')
        editUsername = request.POST.get('editUsername')
        editPassword = request.POST.get('editPassword')
        editName = request.POST.get('editName')
        editLastName = request.POST.get('editLastName')
        editEmail = request.POST.get('editEmail')
        editPhone = request.POST.get('editPhone')
        editRole = request.POST.get('editRole')

        editUser = User.objects.get(id=editIdUser)
        if editUsername == editUser.username:
            editUser.username = editUsername
            editUser.set_password(editPassword)
            editUser.first_name = editName
            editUser.last_name = editLastName
            editUser.email = editEmail
            editUser.save()
            
            editExtendedUser = extendedUser.objects.get(asociatedUser=editUser)
            editExtendedUser.nameUser = editName
            editExtendedUser.lastnameUser = editLastName
            editExtendedUser.phoneUser = editPhone
            editRoleUser = rolesxUser.objects.get(nameRole=editRole)
            editExtendedUser.roleUser = editRoleUser
            editExtendedUser.save()
            return HttpResponseRedirect(reverse('usersMetalprotec:usersMetalprotec'))
        else:
            if checkUsernameExist(editUsername):
                return HttpResponseRedirect(reverse('usersMetalprotec:usersMetalprotec'))
            else:
                editUser.username = editUsername
                editUser.set_password(editPassword)
                editUser.first_name = editName
                editUser.last_name = editLastName
                editUser.email = editEmail
                editUser.save()
                
                editExtendedUser = extendedUser.objects.get(asociatedUser=editUser)
                editExtendedUser.nameUser = editName
                editExtendedUser.lastnameUser = editLastName
                editExtendedUser.phoneUser = editPhone
                editRoleUser = rolesxUser.objects.get(nameRole=editRole)
                editExtendedUser.roleUser = editRoleUser
                editExtendedUser.save()
                return HttpResponseRedirect(reverse('usersMetalprotec:usersMetalprotec'))

@login_required(login_url='/')
def getUserData(request):
    idUser = request.GET.get('idUser')
    editUser = User.objects.get(id=idUser)
    return JsonResponse({
        'editUsername':editUser.username,
        'editName':editUser.first_name,
        'editLastName':editUser.last_name,
        'editEmail':editUser.email,
        'editPhone':editUser.extendeduser.phoneUser,
        'editRole':editUser.extendeduser.roleUser.nameRole,
    })

@login_required(login_url='/')
def logoutSystem(request):
    logout(request)
    return HttpResponseRedirect(reverse('usersMetalprotec:loginSystem'))
