document.addEventListener('DOMContentLoaded', ()=>{
    $('#billsTable').DataTable({
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

    $('#productsCreditNote').on('click', 'input[type="button"]', function(e){
        $(this).closest('tr').remove()
    })

})

function chargeProductsCreditNote(idBill)
{
    idBill = idBill.substring(4)
    document.getElementById('idBill').value = idBill
    fetch(`/salesMetalprotecgetBillProducts?idBill=${idBill}`)
    .then(response => response.json())
    .then(data => {

        cuerpoTabla = document.getElementById('productsCreditNote')
        for(let i = 0; i < data.totalProducts.length; i++ )
        {
            cuerpoTabla.innerHTML += `
                <tr class="text-center align-items-center">
                    <td style="width:160px;"><input type="text" readonly class="form-control" name='codigoProducto' value="${data.totalProducts[i][1]}"></td>
                    <td style="width:280px;"><input type="text" readonly class="form-control" value="${data.totalProducts[i][0]}"></td>
                    <td style="width:100px;"><input type="text" class="form-control" name='cantidadProducto' value="${data.totalProducts[i][2]}"></td>
                    <td><input type="button" class="btn btn-secondary" value="Eliminar"></td>
                </tr>
            `
        }
        console.log(data)
    })
}

function cleanModalCreditNote()
{
    document.getElementById('idBill').value = ''
    document.getElementById('creditNotePurpose').selectedIndex = '0'
    $('creditNotePurpose').selectpicker('refresh')

    document.getElementById('productsCreditNote').innerHTML = ''
}