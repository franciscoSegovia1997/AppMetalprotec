document.addEventListener('DOMContentLoaded', ()=>{
    $('#paymentsTable').DataTable({
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

    selectedClient = document.getElementById('selectedClient')

    selectedClient.onchange = function()
    {
        if(selectedClient.value !== '')
        {
            fetch(`/financeMetalprotecgetDocuments?selectedClient=${selectedClient.value}`)
            .then(response => response.json())
            .then(data => {
                selectedDocument = document.getElementById('selectedDocument')
                while(selectedDocument.length > 0)
                {
                    selectedDocument.remove(0)
                }
                firstOption = document.createElement('option')
                firstOption.value = ''
                firstOption.innerHTML = ''
                selectedDocument.appendChild(firstOption)
                console.log(data)
                for(let i = 0;i < data.finalDocuments.length; i++)
                {
                    newOption = document.createElement('option')
                    newOption.value = data.finalDocuments[i]
                    newOption.innerHTML = data.finalDocuments[i]
                    selectedDocument.appendChild(newOption)
                }
                selectedDocument.selectedIndex='0'
                $('#selectedDocument').selectpicker('refresh')
            })

        }
        else
        {
            selectedDocument = document.getElementById('selectedDocument')
            while(selectedDocument.length > 0)
            {
                selectedDocument.remove(0)
            }

            firstOption = document.createElement('option')
            firstOption.value = ''
            firstOption.innerHTML = ''
            selectedDocument.appendChild(firstOption)
            selectedDocument.selectedIndex = '0'
            $('#selectedDocument').selectpicker('refresh')
        }
    }

    selectedDocument = document.getElementById('selectedDocument')

    selectedDocument.onchange = function()
    {
        if(selectedDocument.value !== '')
        {
            fetch(`/financeMetalprotecgetRelatedDocuments?documentCode=${selectedDocument.value}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('guideInfo').value = data.guideCode
                document.getElementById('quotationInfo').value = data.quotationCode
                document.getElementById('sellerInfo').value = data.userCode
            })
        }
        else
        {
            document.getElementById('guideInfo').value = ''
            document.getElementById('quotationInfo').value = ''
            document.getElementById('sellerInfo').value = ''

        }
    }
})

function cleanNewPayment()
{
    selectedBank = document.getElementById('selectedBank')
    selectedBank.selectedIndex = '0'
    $('#selectedBank').selectpicker('refresh')

    document.getElementById('operationNumber').value = ''
    document.getElementById('operationNumber2').value = ''

    selectedClient = document.getElementById('selectedClient')
    selectedClient.selectedIndex = '0'
    $('#selectedClient').selectpicker('refresh')

    paidDocument = document.getElementById('paidDocument')
    paidDocument.checked = false

    enabledComission = document.getElementById('enabledComission')
    enabledComission.checked = false

    datePayment = document.getElementById('datePayment')
    datePayment.value = '2023-01-01'

    selectedDocument = document.getElementById('selectedDocument')
    while(selectedDocument.length > 0)
    {
        selectedDocument.remove(0)
    }
    firstOption = document.createElement('option')
    firstOption.value = ''
    firstOption.innerHTML = ''
    selectedDocument.appendChild(firstOption)
    selectedDocument.selectedIndex='0'
    $('#selectedDocument').selectpicker('refresh')

    document.getElementById('guideInfo').value = ''
    document.getElementById('quotationInfo').value = ''
    document.getElementById('sellerInfo').value = ''
}

function chargeEditData(idPayment)
{
    idPayment = idPayment.slice(4)
    document.getElementById('idPayment').value = idPayment
    fetch(`/financeMetalprotecgetPaymentData?idPayment=${idPayment}`)
    .then(response => response.json())
    .then(data => {

        document.getElementById('editDate').value = data.editDate
        document.getElementById('editNumber').value = data.editNumber
        document.getElementById('editNumber2').value = data.editNumber2
        document.getElementById('editClient').value = data.editClient
        document.getElementById('editDocument').value = data.editDocument
        document.getElementById('editGuide').value = data.guideInfo
        document.getElementById('editQuotation').value = data.quotationInfo
        document.getElementById('editSeller').value = data.sellerInfo

        if(data.editPaid === 'CANCELADO')
        {
            document.getElementById('editPaid').checked = true
        }
        else 
        {
            document.getElementById('editPaid').checked = false
        }

        if(data.editComission === 'ON')
        {
            document.getElementById('editComission').checked = true
        }
        else
        {
            document.getElementById('editComission').checked = false
        }

        editBank = document.getElementById('editBank')
        for(let i = 0; i < editBank.options.length; i++ )
        {
            if(editBank.options[i].value === data.idBank)
            {
                editBank.selectedIndex = String(i)
                $('#editBank').selectpicker('refresh')
                break;
            }
        }
    })
}

function cleanEditPayment()
{
    document.getElementById('idPayment').value = ''
    
    editBank = document.getElementById('editBank')
    editBank.selectedIndex = '0'
    $('#editBank').selectpicker('refresh')

    document.getElementById('editNumber').value = ''
    document.getElementById('editNumber2').value = ''
    document.getElementById('editClient').value = ''
    document.getElementById('editPaid').checked = false
    document.getElementById('editDocument').value = ''
    document.getElementById('editGuide').value = ''
    document.getElementById('editQuotation').value = ''
    document.getElementById('editSeller').value = ''
    document.getElementById('editDate').value = '2023-01-01'
    document.getElementById('editComission').checked = false

}