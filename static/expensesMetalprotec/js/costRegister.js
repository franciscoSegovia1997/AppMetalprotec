function chargeAsignData(idAsignar)
{
    idRegistro = idAsignar.substring(7)
    registerxBoxInfo = document.getElementById('registerxBoxInfo')
    registerxBoxInfo.value = idRegistro
}

function cleanInfoRegister()
{
    identificationCost=document.getElementById('identificationCost')
    dateRegistered=document.getElementById('dateRegistered')
    rucCost=document.getElementById('rucCost')
    descriptionCost=document.getElementById('descriptionCost')
    valueCost=document.getElementById('valueCost')
    currencyCost=document.getElementById('currencyCost')
    
    divisioInfo = document.getElementById('divisionInfo')
    categoryInfo=document.getElementById('categoryInfo')
    deparmentCost=document.getElementById('deparmentCost')
    typeInfo=document.getElementById('typeInfo')
    behaviorInfo=document.getElementById('behaviorInfo')
    operativeCost=document.getElementById('operativeCost')

    identificationCost.value=''
    dateRegistered.value='2023-01-01'
    rucCost.value=''
    descriptionCost.value=''
    valueCost.value='0.00'

    operativeCost.value=''
    behaviorInfo.value=''
    typeInfo.value=''
    deparmentCost.value=''
    categoryInfo.value = ''

    currencyCost.selectedIndex='0'
    $('#currencyCost').selectpicker('refresh')
    
    divisioInfo.selectedIndex = '0'
    $('#divisionInfo').selectpicker('refresh')
}

document.addEventListener('DOMContentLoaded',()=>{
    $('#costTable').DataTable({
        paging: true,
        pageLength: 20,
        lenghtChange: true,
        autoWidth: false,
        serching: true,
        bInfo: false,
        bSort: false,
        language: {
            "decimal": "",
            "emptyTable": "No hay información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
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

    divisioInfo = document.getElementById('divisionInfo')
    categoryInfo=document.getElementById('categoryInfo')
    deparmentCost=document.getElementById('deparmentCost')
    typeInfo=document.getElementById('typeInfo')
    behaviorInfo=document.getElementById('behaviorInfo')
    operativeCost=document.getElementById('operativeCost')
    
    divisioInfo.onchange = function()
    {
        if(divisioInfo.value === '')
        {
            categoryInfo.value=''
            deparmentCost.value=''
            typeInfo.value=''
            behaviorInfo.value=''
            operativeCost.value=''
        }
        else
        {
            fetch(`/expensesMetalprotecgetDivisionData?idDivision=${divisioInfo.value}`)
            .then(response => response.json())
            .then(data => {
                categoryInfo.value = data.categoryInfo
                deparmentCost.value = data.deparmentInfo
                typeInfo.value = data.typeCost
                behaviorInfo.value = data.behavior
                operativeCost.value = data.operativeCost
            })
        }
    }
})


function showDataRegister(registroId)
{
    razonCosto = document.getElementById('razonCosto')
    fechaCosto = document.getElementById('fechaCosto')
    rucCosto = document.getElementById('rucCosto')
    conceptoCosto = document.getElementById('conceptoCosto')
    importeCosto = document.getElementById('importeCosto')
    monedaCosto = document.getElementById('monedaCosto')
    divisionCosto = document.getElementById('divisionCosto')
    categoriaCosto = document.getElementById('categoriaCosto')
    departamentoCosto = document.getElementById('departamentoCosto')
    tipoCosto = document.getElementById('tipoCosto')
    comportamientoCosto = document.getElementById('comportamientoCosto')
    operativoCosto = document.getElementById('operativoCosto')

    fetch(`/expensesMetalprotecgetDataRegisterInfo?idRegisterInfo=${registroId}`)
    .then(response => response.json())
    .then(data => {
        razonCosto.value = data.razonCosto
        fechaCosto.value = data.fechaCosto
        rucCosto.value = data.rucCosto
        conceptoCosto.value = data.conceptoCosto
        importeCosto.value = data.importeCosto
        monedaCosto.value = data.monedaCosto
        divisionCosto.value = data.divisionCosto
        categoriaCosto.value = data.categoriaCosto
        departamentoCosto.value = data.departamentoCosto
        tipoCosto.value = data.tipoCosto
        comportamientoCosto.value = data.comportamientoCosto
        operativoCosto.value = data.operativoCosto
    })
}


function limpiarInfo()
{
    razonCosto = document.getElementById('razonCosto')
    fechaCosto = document.getElementById('fechaCosto')
    rucCosto = document.getElementById('rucCosto')
    conceptoCosto = document.getElementById('conceptoCosto')
    importeCosto = document.getElementById('importeCosto')
    monedaCosto = document.getElementById('monedaCosto')
    
    divisionCosto = document.getElementById('divisionCosto')
    categoriaCosto = document.getElementById('categoriaCosto')
    departamentoCosto = document.getElementById('departamentoCosto')
    tipoCosto = document.getElementById('tipoCosto')
    comportamientoCosto = document.getElementById('comportamientoCosto')
    operativoCosto = document.getElementById('operativoCosto')

    razonCosto.value = ''
    fechaCosto.value = ''
    rucCosto.value = ''
    conceptoCosto.value = ''
    importeCosto.value = ''
    monedaCosto.value = ''
    divisionCosto.value = ''
    categoriaCosto.value = ''
    departamentoCosto.value = ''
    tipoCosto.value = ''
    comportamientoCosto.value = ''
    operativoCosto.value = ''
}

function cleanDataBoxInfo()
{
    idBoxInfo = document.getElementById('idBoxInfo')
    registerxBoxInfo = document.getElementById('registerxBoxInfo')

    registerxBoxInfo.value = ''
    idBoxInfo.selectedIndex='0'
    $('#idBoxInfo').selectpicker('refresh')
}