document.addEventListener('DOMContentLoaded', ()=>{
    incomingInfoTable = $('#incomingInfoTable').DataTable({
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

    filterIncomingData = document.getElementById('filterIncomingData')

    filterIncomingData.onclick = function()
    {
        startDate = document.getElementById('startDate')
        endDate = document.getElementById('endDate')
        incomingInfoTable.clear().draw()
        if(startDate.value !== '' && endDate.value !== '')
        {
            incomingInfoTable.clear().draw()
            fetch(`/stockManagmentfilterIncomingItemsJson?startDate=${startDate.value}&endDate=${endDate.value}`)
            .then(response => response.json())
            .then(data => {
                for(let i = 0; i < data.incomingData.length; i++)
                {
                    comisionTable.row.add(data.incomingData[i]).draw()
                }
            })
        }
        else
        {
            console.log('INGRESE LAS FECHAS CORRECTAMENTE')
        }        
    }
})