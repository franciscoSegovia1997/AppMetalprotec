document.addEventListener('DOMContentLoaded',()=>{
    selectedDeparment = document.getElementById('selectedDeparment')
    selectedCategory = document.getElementById('selectedCategory')

    selectedDeparment.onchange = function()
    {
        idDeparment = selectedDeparment.value
        if(idDeparment !== '')
        {
            fetch(`/expensesMetalprotecgetCategories?idDeparment=${idDeparment}`)
            .then(response => response.json())
            .then(data => {
                while(selectedCategory.length > 0)
                {
                    selectedCategory.remove(0)
                }

                newOption = document.createElement('option')
                newOption.value = ''
                newOption.innerHTML = ''
                selectedCategory.appendChild(newOption)

                for(let i = 0; i < data.categoriesxDeparment.length;i++)
                {
                    mensaje = ""
                    createdOption = document.createElement('option')
                    createdOption.value = data.categoriesxDeparment[i][0]
                    createdOption.innerHTML = data.categoriesxDeparment[i][1]
                    selectedCategory.appendChild(createdOption)
                }
                selectedCategory.selectedIndex = '0'
                $('#selectedCategory').selectpicker('refresh')
            })
        }
        else
        {
            while(selectedCategory.length > 0)
            {
                selectedCategory.remove(0)
            }

            newOption = document.createElement('option')
            newOption.value = ''
            newOption.innerHTML = ''
            selectedCategory.appendChild(newOption)
            selectedCategory.selectedIndex = '0'
            $('#selectedCategory').selectpicker('refresh')
        }
        
    }

    $('#divisionsTable').DataTable({
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
})

function deleteRegisterDeparment()
{
    document.getElementById('nameDeparment').value=''
}

function deleteRegisterCategory()
{
    idDeparment = document.getElementById('idDeparment')
    idDeparment.selectedIndex='0'
    $('#idDeparment').selectpicker('refresh')

    document.getElementById('nameCategory').value=''
}

function deleteRegisterDivision()
{
    selectedDeparment=document.getElementById('selectedDeparment')
    selectedCategory=document.getElementById('selectedCategory')
    nameDivision=document.getElementById('nameDivision')
    typeCost=document.getElementById('typeCost')
    behavior=document.getElementById('behavior')
    operativeCost=document.getElementById('operativeCost')

    while(selectedCategory.length > 0)
    {
        selectedCategory.remove(0)
    }

    newOption = document.createElement('option')
    newOption.value = ''
    newOption.innerHTML = ''
    selectedCategory.appendChild(newOption)
    selectedCategory.selectedIndex = '0'
    $('#selectedCategory').selectpicker('refresh')

    operativeCost.selectedIndex='0'
    $('#operativeCost').selectpicker('refresh')

    behavior.selectedIndex = '0'
    $('#behavior').selectpicker('refresh')

    typeCost.selectedIndex = '0'
    $('#typeCost').selectpicker('refresh')

    nameDivision.value = ''

    selectedDeparment.selectedIndex = '0'
    $('#selectedDeparment').selectpicker('refresh')
}