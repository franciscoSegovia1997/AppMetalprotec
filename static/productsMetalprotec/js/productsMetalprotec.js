document.addEventListener('DOMContentLoaded', ()=>{
    $('#productsTable').DataTable({
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

function deleteNewProductInfo()
{
    nameProduct=document.getElementById('nameProduct')
    measureUnit=document.getElementById('measureUnit')
    codeProduct=document.getElementById('codeProduct')
    codeSunatProduct=document.getElementById('codeSunatProduct')
    categoryProduct=document.getElementById('categoryProduct')
    subCategoryProduct=document.getElementById('subCategoryProduct')
    pvnIGV=document.getElementById('pvnIGV')
    pcnIGV=document.getElementById('pcnIGV')
    weightProduct=document.getElementById('weightProduct')
    currencyProduct=document.getElementById('currencyProduct')
    kitProduct=document.getElementById('kitProduct')

    nameProduct.value=''
    measureUnit.value=''
    codeProduct.value=''
    codeSunatProduct.value=''
    categoryProduct.value=''
    subCategoryProduct.value=''
    pvnIGV.value=''
    pcnIGV.value=''
    weightProduct.value=''
    currencyProduct.selectedIndex='0'
    kitProduct.checked = false
    $('#currencyProduct').selectpicker('refresh')

}

function deleteDeleteInfo()
{
    deleteIdProduct = document.getElementById('deleteIdProduct')
    deleteIdProduct.value = ''
}

function loadDeleteData(idProduct)
{
    deleteIdProduct = document.getElementById('deleteIdProduct')
    deleteIdProduct.value = ''
    idProduct = idProduct.slice(6)
    deleteIdProduct.value = idProduct
}

function deleteEditProductInfo()
{
    editIdProduct=document.getElementById('editIdProduct')
    editNameProduct=document.getElementById('editNameProduct')
    editMeasureUnit=document.getElementById('editMeasureUnit')
    editCodeProduct=document.getElementById('editCodeProduct')
    editCodeSunatProduct=document.getElementById('editCodeSunatProduct')
    editCategoryProduct=document.getElementById('editCategoryProduct')
    editSubCategoryProduct=document.getElementById('editSubCategoryProduct')
    editPvnIGV=document.getElementById('editPvnIGV')
    editPcnIGV=document.getElementById('editPcnIGV')
    editWeightProduct=document.getElementById('editWeightProduct')
    editCurrencyProduct=document.getElementById('editCurrencyProduct')
    editKit=document.getElementById('editKit')

    editIdProduct.value=''
    editNameProduct.value=''
    editMeasureUnit.value=''
    editCodeProduct.value=''
    editCodeSunatProduct.value=''
    editCategoryProduct.value=''
    editSubCategoryProduct.value=''
    editPvnIGV.value=''
    editPcnIGV.value=''
    editWeightProduct.value=''
    editKit.checked = false
    editCurrencyProduct.selectedIndex='0'
    $('#editCurrencyProduct').selectpicker('refresh')
}

function loadEditProductData(idProduct)
{
    editIdProduct=document.getElementById('editIdProduct')
    editNameProduct=document.getElementById('editNameProduct')
    editMeasureUnit=document.getElementById('editMeasureUnit')
    editCodeProduct=document.getElementById('editCodeProduct')
    editCodeSunatProduct=document.getElementById('editCodeSunatProduct')
    editCategoryProduct=document.getElementById('editCategoryProduct')
    editSubCategoryProduct=document.getElementById('editSubCategoryProduct')
    editPvnIGV=document.getElementById('editPvnIGV')
    editPcnIGV=document.getElementById('editPcnIGV')
    editWeightProduct=document.getElementById('editWeightProduct')
    editCurrencyProduct=document.getElementById('editCurrencyProduct')
    editKit=document.getElementById('editKit')

    editIdProduct.value=''
    editNameProduct.value=''
    editMeasureUnit.value=''
    editCodeProduct.value=''
    editCodeSunatProduct.value=''
    editCategoryProduct.value=''
    editSubCategoryProduct.value=''
    editPvnIGV.value=''
    editPcnIGV.value=''
    editWeightProduct.value=''
    editCurrencyProduct.selectedIndex='0'
    $('#editCurrencyProduct').selectpicker('refresh')

    idProduct = idProduct.slice(4)
    editIdProduct.value=idProduct

    fetch(`/productsMetalprotecgetProductData?idProduct=${idProduct}`)
    .then(response => response.json())
    .then(data => {
        editNameProduct.value=data.editNameProduct
        editMeasureUnit.value=data.editMeasureUnit
        editCodeProduct.value=data.editCodeProduct
        editCodeSunatProduct.value=data.editCodeSunatProduct
        editCategoryProduct.value=data.editCategoryProduct
        editSubCategoryProduct.value=data.editSubCategoryProduct
        editPvnIGV.value=data.editPvnIGV
        editPcnIGV.value=data.editPcnIGV
        editWeightProduct.value=data.editWeightProduct

        for(let i = 0; i < editCurrencyProduct.options.length; i++ )
        {
            if(editCurrencyProduct.options[i].value === data.editCurrencyProduct)
            {
                editCurrencyProduct.selectedIndex = String(i)
                $('#editCurrencyProduct').selectpicker('refresh')
                break;
            }
        }

        if(data.editKit === 'ON')
        {
            editKit.checked = true
        }
        else
        {
            editKit.checked = false
        }
    })
}

function deleteShowStockProduct()
{
    stockStoreProduct=document.getElementById('stockStoreProduct')
    stockStoreProduct.innerHTML = ''
}

function loadShowStockData(idProduct)
{
    idProduct=idProduct.slice(4)
    stockStoreProduct=document.getElementById('stockStoreProduct')
    stockStoreProduct.innerHTML = ''
    fetch(`/productsMetalprotecgetProductStock?idProduct=${idProduct}`)
    .then(response => response.json())
    .then(data => {
        for(let i = 0;i < data.stockStoreProduct.length; i++)
        {
            nuevaFila = `
                      <tr>
                        <td>${data.stockStoreProduct[i][0]}</td>
                        <td>${data.stockStoreProduct[i][1]}</td>
                      </tr>
                      `
            stockStoreProduct.innerHTML += nuevaFila
        }
    })
}

function deleteAddStockInfo()
{
    addStockIdProduct = document.getElementById('addStockIdProduct')
    addStockIdStore = document.getElementById('addStockIdStore')
    addStockQt = document.getElementById('addStockQt')

    addStockIdProduct.selectedIndex = '0'
    $('#addStockIdProduct').selectpicker('refresh')
    addStockIdStore.selectedIndex = '0'
    $('#addStockIdStore').selectpicker('refresh')
    addStockQt.value = ''
}

function chargeKitInfo(idProduct)
{
    idProduct = idProduct.slice(3)
    kitInfoProduct = document.getElementById('kitInfoProduct')
    kitInfoProduct.innerHTML = ''
    idProductKit = document.getElementById('idProductKit')
    idProductKit.value = ''

    idProductKit.value = idProduct
    fetch(`/productsMetalprotecgetProductKit?idProduct=${idProduct}`)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        for(let i = 0;i < data.arrayKit.length; i++)
        {
            nuevaFila = `
                      <tr>
                        <td>${data.arrayKit[i][0]}</td>
                        <td>${data.arrayKit[i][1]}</td>
                      </tr>
                      `
            kitInfoProduct.innerHTML += nuevaFila
        }

        if(data.arrayKit.length > 4)
        {
            document.getElementById('newProductKitSection').style.display = 'none'
        }
        else
        {
            document.getElementById('newProductKitSection').style.display = ''
        }
    })
}

function deleteKitInfoProduct()
{
    kitInfoProduct = document.getElementById('kitInfoProduct')
    newProductKit = document.getElementById('newProductKit')
    qtProductKit = document.getElementById('qtProductKit')
    idProductKit = document.getElementById('idProductKit')

    idProductKit.value = ''
    kitInfoProduct.innerHTML = ''
    qtProductKit.value = ''
    newProductKit.selectedIndex = '0'
    $('#newProductKit').selectpicker('refresh')
}