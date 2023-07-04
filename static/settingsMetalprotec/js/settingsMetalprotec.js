document.addEventListener('DOMContentLoaded', ()=>{
    $('#endpointsTable').DataTable({
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
    serieCoti=document.getElementById('serieCoti')
    nroCoti=document.getElementById('nroCoti')
    serieGuia=document.getElementById('serieGuia')
    nroGuia=document.getElementById('nroGuia')
    serieFactura=document.getElementById('serieFactura')
    nroFactura=document.getElementById('nroFactura')
    serieBoleta=document.getElementById('serieBoleta')
    nroBoleta=document.getElementById('nroBoleta')
    serieNotaFactura=document.getElementById('serieNotaFactura')
    nroNotaFactura=document.getElementById('nroNotaFactura')
    serieNotaBoleta=document.getElementById('serieNotaBoleta')
    nroNotaBoleta=document.getElementById('nroNotaBoleta')

    serieCoti.value=''
    nroCoti.value=''
    serieGuia.value=''
    nroGuia.value=''
    serieFactura.value=''
    nroFactura.value=''
    serieBoleta.value=''
    nroBoleta.value=''
    serieNotaFactura.value=''
    nroNotaFactura.value=''
    serieNotaBoleta.value=''
    nroNotaBoleta.value=''
}

function deleteEditInfo()
{
    editIdEndpoint=document.getElementById('editIdEndpoint')
    editSerieCoti=document.getElementById('editSerieCoti')
    editNroCoti=document.getElementById('editNroCoti')
    editSerieGuia=document.getElementById('editSerieGuia')
    editNroGuia=document.getElementById('editNroGuia')
    editSerieFactura=document.getElementById('editSerieFactura')
    editNroFactura=document.getElementById('editNroFactura')
    editSerieBoleta=document.getElementById('editSerieBoleta')
    editNroBoleta=document.getElementById('editNroBoleta')
    editSerieNotaFactura=document.getElementById('editSerieNotaFactura')
    editNroNotaFactura=document.getElementById('editNroNotaFactura')
    editSerieNotaBoleta=document.getElementById('editSerieNotaBoleta')
    editNroNotaBoleta=document.getElementById('editNroNotaBoleta')

    editIdEndpoint.value=''
    editSerieCoti.value=''
    editNroCoti.value=''
    editSerieGuia.value=''
    editNroGuia.value=''
    editSerieFactura.value=''
    editNroFactura.value=''
    editSerieBoleta.value=''
    editNroBoleta.value=''
    editSerieNotaFactura.value=''
    editNroNotaFactura.value=''
    editSerieNotaBoleta.value=''
    editNroNotaBoleta.value=''
}

function loadEditData(idEndpoint)
{
    idEndpoint = idEndpoint.slice(4)
    
    editIdEndpoint=document.getElementById('editIdEndpoint')
    editIdEndpoint.value = idEndpoint

    editSerieCoti=document.getElementById('editSerieCoti')
    editNroCoti=document.getElementById('editNroCoti')
    editSerieGuia=document.getElementById('editSerieGuia')
    editNroGuia=document.getElementById('editNroGuia')
    editSerieFactura=document.getElementById('editSerieFactura')
    editNroFactura=document.getElementById('editNroFactura')
    editSerieBoleta=document.getElementById('editSerieBoleta')
    editNroBoleta=document.getElementById('editNroBoleta')
    editSerieNotaFactura=document.getElementById('editSerieNotaFactura')
    editNroNotaFactura=document.getElementById('editNroNotaFactura')
    editSerieNotaBoleta=document.getElementById('editSerieNotaBoleta')
    editNroNotaBoleta=document.getElementById('editNroNotaBoleta')

    editSerieCoti.value=''
    editNroCoti.value=''
    editSerieGuia.value=''
    editNroGuia.value=''
    editSerieFactura.value=''
    editNroFactura.value=''
    editSerieBoleta.value=''
    editNroBoleta.value=''
    editSerieNotaFactura.value=''
    editNroNotaFactura.value=''
    editSerieNotaBoleta.value=''
    editNroNotaBoleta.value=''

    fetch(`/settingsMetalprotecgetEndpointData?idEndpoint=${idEndpoint}`)
    .then(response => response.json())
    .then(data => {

        editSerieCoti.value=data.editSerieCoti
        editNroCoti.value=data.editNroCoti
        editSerieGuia.value=data.editSerieGuia
        editNroGuia.value=data.editNroGuia
        editSerieFactura.value=data.editSerieFactura
        editNroFactura.value=data.editNroFactura
        editSerieBoleta.value=data.editSerieBoleta
        editNroBoleta.value=data.editNroBoleta
        editSerieNotaFactura.value=data.editSerieNotaFactura
        editNroNotaFactura.value=data.editNroNotaFactura
        editSerieNotaBoleta.value=data.editSerieNotaBoleta
        editNroNotaBoleta.value=data.editNroNotaBoleta
    })
}

function deleteDeleteInfo()
{
    deleteIdEndpoint = document.getElementById('deleteIdEndpoint')
    deleteIdEndpoint.value = ''
}

function loadDeleteData(idEndpoint)
{
    deleteIdEndpoint = document.getElementById('deleteIdEndpoint')
    deleteIdEndpoint.value = ''
    idEndpoint = idEndpoint.slice(6)
    deleteIdEndpoint.value = idEndpoint
}