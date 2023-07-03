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

function loadEditData(editIdUser)
{
    console.log(editIdUser)
}