document.addEventListener('DOMContentLoaded', ()=>{
    outcomingInfoTable = $('#outcomingInfoTable').DataTable({
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

    filterOutcomingData = document.getElementById('filterOutcomingData')

    filterOutcomingData.onclick = function()
    {
        startDate = document.getElementById('startDate')
        endDate = document.getElementById('endDate')
        outcomingInfoTable.clear().draw()
        if(startDate.value !== '' && endDate.value !== '')
        {
            outcomingInfoTable.clear().draw()
            fetch(`/stockManagmentfilterOutcomingItemsJson?startDate=${startDate.value}&endDate=${endDate.value}`)
            .then(response => response.json())
            .then(data => {
                for(let i = 0; i < data.outcomingData.length; i++)
                {
                    outcomingInfoTable.row.add(data.outcomingData[i]).draw()
                }
            })
        }
        else
        {
            console.log('INGRESE LAS FECHAS CORRECTAMENTE')
        }        
    }
})