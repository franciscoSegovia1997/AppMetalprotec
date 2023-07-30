
function deleteNewComission()
{
    console.log('Hola a todos')
    selectedUserComission =document.getElementById('selectedUserComission')
    percentageComission = document.getElementById('percentageComission')
    igvIncluded = document.getElementById('igvIncluded')

    selectedUserComission.selectedIndex = '0'
    $('#selectedUserComission').selectpicker('refresh')
    percentageComission.value = ''
    igvIncluded.checked = false
}

function agregarUsuarioComision()
{
    usuariosComisiones = document.getElementById('usuariosComisiones')
    asociatedUser = document.getElementById('asociatedUser')
    globalPercentage = document.getElementById('globalPercentage')
    globalIgv = document.getElementById('globalIgv')

    if(globalIgv.checked === true)
    {
        userxIgv = 'ON'
    }
    else
    {
        userxIgv = 'OFF'
    }

    nuevaFila = `
        <tr>
            <td style='display:none;'><input class='form-control' name='idAsociatedUserInfo' value='${asociatedUser.value}'></td>
            <td><input class='form-control' name='globalUsernameInfo' value='${asociatedUser.options[asociatedUser.selectedIndex].text}' readonly></td>
            <td><input class='form-control' name='globalPercentageInfo' value='${globalPercentage.value}'></td>
            <td><input class='form-control' name='globalIgvIncludedInfo' value='${userxIgv}' readonly></td>
            <td><input type='button' class='btn btn-danger' value='Eliminar'></td>
        </tr>`
    usuariosComisiones.innerHTML += nuevaFila

    globalIgv.checked = false
    asociatedUser.selectedIndex = '0'
    $('#asociatedUser').selectpicker('refresh')
    globalPercentage.value = ''
}

function deleteGlobalComission()
{
    usuariosComisiones = document.getElementById('usuariosComisiones')
    usuariosComisiones.innerHTML = ''

    mainUser = document.getElementById('mainUser')
    asociatedUser = document.getElementById('asociatedUser')
    globalPercentage = document.getElementById('globalPercentage')
    globalIgv = document.getElementById('globalIgv')

    globalIgv.checked = false
    globalPercentage.value = ''
    asociatedUser.selectedIndex = '0'
    $('#asociatedUser').selectpicker('refresh')
    mainUser.selectedIndex = '0'
    $('#mainUser').selectpicker('refresh')
}

document.addEventListener('DOMContentLoaded',()=>{
    $('#usuariosComisiones').on('click', 'input[type="button"]', function(e){
        $(this).closest('tr').remove()
    })
})
