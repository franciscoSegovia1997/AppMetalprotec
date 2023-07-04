document.addEventListener('DOMContentLoaded', ()=>{
    $('#usersTable').DataTable({
        paging: true,
        pageLength: 20,
        lenghtChange: true,
        autoWidth: false,
        serching: true,
        bInfo: false,
        bSort: false,
        language: {
            "decimal": "",
            "emptyTable": "Sin información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Sin entradas",
            "infoFiltered": "(Filtrado de _MAX_ total entradas)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ Entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Sin resultados encontrados",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        }
    })
})

function deleteNewInfo()
{
    newUsername=document.getElementById('newUsername')
    newPassword=document.getElementById('newPassword')
    newName=document.getElementById('newName')
    newLastName=document.getElementById('newLastName')
    newEmail=document.getElementById('newEmail')
    newPhone=document.getElementById('newPhone')
    newRole=document.getElementById('newRole')

    newUsername.value=''
    newPassword.value=''
    newName.value=''
    newLastName.value=''
    newEmail.value=''
    newPhone.value=''
    newRole.selectedIndex = '0'
    $('#newRole').selectpicker('refresh')
}

function deleteEditInfo()
{
    editIdUser=document.getElementById('editIdUser')
    editUsername=document.getElementById('editUsername')
    editPassword=document.getElementById('editPassword')
    editName=document.getElementById('editName')
    editLastName=document.getElementById('editLastName')
    editEmail=document.getElementById('editEmail')
    editPhone=document.getElementById('editPhone')
    editRole=document.getElementById('editRole')

    editIdUser.value=''
    editUsername.value=''
    editPassword.value=''
    editName.value=''
    editLastName.value=''
    editEmail.value=''
    editPhone.value=''
    editRole.selectedIndex = '0'
    $('#editRole').selectpicker('refresh')
}

function loadEditData(idUser)
{
    idUser = idUser.slice(4)
    
    editIdUser=document.getElementById('editIdUser')
    editIdUser.value = idUser

    editUsername=document.getElementById('editUsername')
    editPassword=document.getElementById('editPassword')
    editName=document.getElementById('editName')
    editLastName=document.getElementById('editLastName')
    editEmail=document.getElementById('editEmail')
    editPhone=document.getElementById('editPhone')
    editRole=document.getElementById('editRole')

    editUsername.value=''
    editPassword.value=''
    editName.value=''
    editLastName.value=''
    editEmail.value=''
    editPhone.value=''
    editRole.selectedIndex = '0'
    $('#editRole').selectpicker('refresh')

    fetch(`/getUserData?idUser=${idUser}`)
    .then(response => response.json())
    .then(data => {

        editUsername.value=data.editUsername
        editPassword.value=''
        editName.value=data.editName
        editLastName.value=data.editLastName
        editEmail.value=data.editEmail
        editPhone.value=data.editPhone

        for(let i = 0; i < editRole.options.length; i++)
        {
            if(editRole.options[i].value === data.editRole)
            {
                editRole.selectedIndex = String(i)
                $('#editRole').selectpicker('refresh')
                break;
            }
        }
    })
}

function deleteDeleteInfo()
{
    deleteIdUser = document.getElementById('deleteIdUser')
    deleteIdUser.value = ''
}

function loadDeleteData(idUser)
{
    deleteIdUser = document.getElementById('deleteIdUser')
    deleteIdUser.value = ''
    idUser = idUser.slice(6)
    deleteIdUser.value = idUser
}

function deleteAssignInfo()
{
    userEditRole = document.getElementById('userEditRole')
    roleEditRole = document.getElementById('roleEditRole')

    userEditRole.selectedIndex = '0'
    $('#userEditRole').selectpicker('refresh')

    roleEditRole.selectedIndex = '0'
    $('#roleEditRole').selectpicker('refresh')

}

function deleteAssignEndpoint()
{
    userEditEndpoint = document.getElementById('userEditEndpoint')
    endpointEditEndpoint = document.getElementById('endpointEditEndpoint')

    userEditEndpoint.selectedIndex = '0'
    $('#userEditEndpoint').selectpicker('refresh')

    endpointEditEndpoint.selectedIndex = '0'
    $('#endpointEditEndpoint').selectpicker('refresh')

}