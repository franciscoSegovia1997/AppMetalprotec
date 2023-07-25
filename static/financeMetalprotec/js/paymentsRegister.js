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
})