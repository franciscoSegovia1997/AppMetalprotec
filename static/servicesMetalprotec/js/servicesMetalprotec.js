document.addEventListener('DOMContentLoaded', ()=>{
    $('#servicesTable').DataTable({
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
    nameService=document.getElementById('nameService')
    measureUnit=document.getElementById('measureUnit')
    categoryService=document.getElementById('categoryService')
    subCategoryService=document.getElementById('subCategoryService')
    pvnIGV=document.getElementById('pvnIGV')
    currencyService=document.getElementById('currencyService')

    nameService.value=''
    measureUnit.value=''
    categoryService.value=''
    subCategoryService.value=''
    pvnIGV.value=''
    currencyService.selectedIndex='0'
    $('#currencyService').selectpicker('refresh')
}

function deleteEditInfo()
{
    editNameService=document.getElementById('editNameService')
    editMeasureUnit=document.getElementById('editMeasureUnit')
    editCategoryService=document.getElementById('editCategoryService')
    editSubCategoryService=document.getElementById('editSubCategoryService')
    editPvnIGV=document.getElementById('editPvnIGV')
    editCurrencyService=document.getElementById('editCurrencyService')

    editNameService.value=''
    editMeasureUnit.value=''
    editCategoryService.value=''
    editSubCategoryService.value=''
    editPvnIGV.value=''
    editCurrencyService.selectedIndex='0'
    $('#editCurrencyService').selectpicker('refresh')
}

function loadEditData(idService)
{
    idService = idService.slice(4)
    
    editIdService=document.getElementById('editIdService')
    editIdService.value = idService

    editNameService=document.getElementById('editNameService')
    editMeasureUnit=document.getElementById('editMeasureUnit')
    editCategoryService=document.getElementById('editCategoryService')
    editSubCategoryService=document.getElementById('editSubCategoryService')
    editPvnIGV=document.getElementById('editPvnIGV')
    editCurrencyService=document.getElementById('editCurrencyService')

    editNameService.value=''
    editMeasureUnit.value=''
    editCategoryService.value=''
    editSubCategoryService.value=''
    editPvnIGV.value=''
    editCurrencyService.selectedIndex='0'
    $('#editCurrencyService').selectpicker('refresh')

    fetch(`/servicesMetalprotecgetServiceData?idService=${idService}`)
    .then(response => response.json())
    .then(data => {

        editNameService.value=data.editNameService
        editMeasureUnit.value=data.editMeasureUnit
        editCategoryService.value=data.editCategoryService
        editSubCategoryService.value=data.editSubCategoryService
        editPvnIGV.value=data.editPvnIGV

        for(let i = 0; i < editCurrencyService.options.length; i++ )
        {
            if(editCurrencyService.options[i].value === data.editCurrencyService)
            {
                editCurrencyService.selectedIndex = String(i)
                $('#editCurrencyService').selectpicker('refresh')
                break;
            }
        }
    })
}

function deleteDeleteInfo()
{
    deleteIdService = document.getElementById('deleteIdService')
    deleteIdService.value = ''
}

function loadDeleteData(idService)
{
    deleteIdService = document.getElementById('deleteIdService')
    deleteIdService.value = ''
    idService = idService.slice(6)
    deleteIdService.value = idService
}