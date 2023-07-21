document.addEventListener('DOMContentLoaded', ()=>{
    $('#clientsTable').DataTable({
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

function deleteNewClientInfo()
{
    identificationClient=document.getElementById('identificationClient')
    documentClient=document.getElementById('documentClient')
    emailClient=document.getElementById('emailClient')
    legalAddressClient=document.getElementById('legalAddressClient')
    contactClient=document.getElementById('contactClient')
    phoneClient=document.getElementById('phoneClient')
    typeClient=document.getElementById('typeClient')
    enabledCommission=document.getElementById('enabledCommission')

    identificationClient.value=''
    documentClient.value=''
    emailClient.value=''
    legalAddressClient.value=''
    contactClient.value=''
    phoneClient.value=''

    typeClient.selectedIndex='0'
    $('#typeClient').selectpicker('refresh')

    enabledCommission.checked = false
}

function deleteDeleteClientInfo()
{
    deleteIdClient = document.getElementById('deleteIdClient')
    deleteIdClient.value = ''
}

function loadDeleteClientData(idClient)
{
    deleteIdClient = document.getElementById('deleteIdClient')
    deleteIdClient.value = ''
    idClient = idClient.slice(6)
    deleteIdClient.value = idClient
}

function deleteEditClientInfo()
{
    editIdClient=document.getElementById('editIdClient')
    editDocumentClient=document.getElementById('editDocumentClient')
    editIdentificationClient=document.getElementById('editIdentificationClient')
    editTypeClient=document.getElementById('editTypeClient')
    editEmailClient=document.getElementById('editEmailClient')
    editContactClient=document.getElementById('editContactClient')
    editPhoneClient=document.getElementById('editPhoneClient')
    editLegalAddressClient=document.getElementById('editLegalAddressClient')
    editEnabledCommission=document.getElementById('editEnabledCommission')

    editIdClient.value=''
    editDocumentClient.value=''
    editIdentificationClient.value=''
    editEmailClient.value=''
    editContactClient.value=''
    editPhoneClient.value=''
    editLegalAddressClient.value=''

    editTypeClient.selectedIndex='0'
    $('#editTypeClient').selectpicker('refresh')
    editEnabledCommission.checked=false
}

function loadEditClientData(idClient)
{
    editIdClient=document.getElementById('editIdClient')
    editDocumentClient=document.getElementById('editDocumentClient')
    editIdentificationClient=document.getElementById('editIdentificationClient')
    editTypeClient=document.getElementById('editTypeClient')
    editEmailClient=document.getElementById('editEmailClient')
    editContactClient=document.getElementById('editContactClient')
    editPhoneClient=document.getElementById('editPhoneClient')
    editLegalAddressClient=document.getElementById('editLegalAddressClient')
    editEnabledCommission=document.getElementById('editEnabledCommission')

    editIdClient.value=''
    editDocumentClient.value=''
    editIdentificationClient.value=''
    editEmailClient.value=''
    editContactClient.value=''
    editPhoneClient.value=''
    editLegalAddressClient.value=''

    editTypeClient.selectedIndex='0'
    $('#editTypeClient').selectpicker('refresh')
    editEnabledCommission.checked = false

    idClient = idClient.slice(4)
    editIdClient.value=idClient

    fetch(`/clientsMetalprotecgetClientData?idClient=${idClient}`)
    .then(response => response.json())
    .then(data => {
        editDocumentClient.value=data.editDocumentClient
        editIdentificationClient.value=data.editIdentificationClient
        editEmailClient.value=data.editEmailClient
        editContactClient.value=data.editContactClient
        editPhoneClient.value=data.editPhoneClient
        editLegalAddressClient.value=data.editLegalAddressClient

        for(let i = 0; i < editTypeClient.options.length; i++ )
        {
            if(editTypeClient.options[i].value === data.editTypeClient)
            {
                editTypeClient.selectedIndex = String(i)
                $('#editTypeClient').selectpicker('refresh')
                break;
            }
        }

        if( data.editEnabledCommission === 'ON')
        {
            editEnabledCommission.checked=true
        }
        else
        {
            editEnabledCommission.checked=false
        }
    })
}

function deleteShowAddresses()
{
    addressesClient = document.getElementById(id='addressesClient')
    addressesClient.innerHTML=''
}

function loadClientAddress(idClient)
{
    idClient=idClient.slice(4)
    addressesClient = document.getElementById(id='addressesClient')
    addressesClient.innerHTML=''

    fetch(`/clientsMetalprotecgetClientAddress?idClient=${idClient}`)
    .then(response => response.json())
    .then(data => {
        for(let i = 0;i < data.addressesClient.length; i++)
        {
            nuevaFila = `
                      <tr>
                        <td>${data.addressesClient[i]}</td>
                      </tr>
                      `
            addressesClient.innerHTML += nuevaFila
        }
    })
}

function deleteNewAddress()
{
    addAddressClient=document.getElementById('addAddressClient')
    newClientAddress=document.getElementById('newClientAddress')

    newClientAddress.value=''
    addAddressClient.selectedIndex='0'
    $('#addAddressClient').selectpicker('refresh')
}

function getCompanyInfo()
{
    documentClient = document.getElementById('documentClient').value
    fetch(`/clientsMetalprotecgetCompanyInfo?rucInfo=${documentClient}`)
    .then(response => response.json())
    .then(data => {

        document.getElementById('identificationClient').value = data.legalName
        document.getElementById('legalAddressClient').value = data.legalAddress
    })
}