document.addEventListener('DOMContentLoaded', ()=>{
    $('#bankRegistersTable').DataTable({
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

function deleteAllData()
{
    nameBank = document.getElementById('nameBank')
    currencyBank = document.getElementById('currencyBank')
    accountNumber = document.getElementById('accountNumber')
    moneyBank = document.getElementById('moneyBank')

    nameBank.value = ''
    accountNumber.value = ''
    moneyBank.value = ''
    currencyBank.selectedIndex = '0'
    $('#currencyBank').selectpicker('refresh')
}