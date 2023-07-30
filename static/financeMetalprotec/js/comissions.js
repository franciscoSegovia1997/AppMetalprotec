document.addEventListener('DOMContentLoaded', ()=>{
    comisionTable = $('#comisionTable').DataTable({
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

    filterComission = document.getElementById('filterComission')
    userComission = document.getElementById('userComission')
    configComission = document.getElementById('configComission') 

    userComission.onchange = function()
    {
        if(userComission !== '')
        {
            while(configComission.length > 0)
            {
                configComission.remove(0)
            }

            firstOption = document.createElement('option')
            firstOption.value = ''
            firstOption.innerHTML = ''
            configComission.appendChild(firstOption)
            configComission.selectedIndex = '0'
            $('#configComission').selectpicker('refresh')

            fetch(`/financeMetalprotecgetConfigComission?userComission=${userComission.value}`)
            .then(response => response.json())
            .then(data => {
                for(let i = 0;i < data.allConfig.length; i++)
                {
                    newOption = document.createElement('option')
                    newOption.value = data.allConfig[i][0]
                    newOption.innerHTML = data.allConfig[i][1]
                    configComission.appendChild(newOption)
                }
                configComission.selectedIndex = '0'
                $('#configComission').selectpicker('refresh')
            })
        }
        else
        {
            while(configComission.length > 0)
            {
                configComission.remove(0)
            }

            firstOption = document.createElement('option')
            firstOption.value = ''
            firstOption.innerHTML = ''
            configComission.appendChild(firstOption)
            configComission.selectedIndex = '0'
            $('#configComission').selectpicker('refresh')
        }
    }

    filterComission.onclick = function ()
    {

        document.getElementById('sellerCodeInfo').innerHTML = 'VENDEDOR-CODIGO'
        document.getElementById('qtUserInfo').innerHTML = 'CANTIDAD-VENDEDOR'
        document.getElementById('comisionInfoSeller').innerHTML = 'COMISION-VENDEDOR'
        idUserComission = document.getElementById('userComission').value
        configComission = document.getElementById('configComission').value
        monthComission = document.getElementById('monthComission').value
        yearComission = document.getElementById('yearComission').value

        if(idUserComission !== '' && configComission !== '' && monthComission !== '' && yearComission !== '')
        {
            comisionTable.clear().draw()
            fetch(`/financeMetalprotecgetComissionData?idUserComission=${userComission.value}&configComission=${configComission}&monthComission=${monthComission}&yearComission=${yearComission}`)
            .then(response => response.json())
            .then(data => {
                for(let i = 0; i < data.comissionData.length; i++)
                {
                    comisionTable.row.add(data.comissionData[i]).draw()
                }

                document.getElementById('sellerCodeInfo').innerHTML = data.codeUserInfo
                document.getElementById('qtUserInfo').innerHTML = data.finalValue
                document.getElementById('comisionInfoSeller').innerHTML = data.finalComission
            })

        }
        else
        {
            document.getElementById('sellerCodeInfo').innerHTML = 'VENDEDOR-CODIGO'
            document.getElementById('qtUserInfo').innerHTML = 'CANTIDAD-VENDEDOR'
            document.getElementById('comisionInfoSeller').innerHTML = 'COMISION-VENDEDOR'
            comisionTable.clear().draw()
        }
        /*
        Ejemplo de agregar filas a un datatable
        console.log('Agregnado fila')
        nuevaFila = ['2023-07-02', 'BCP', 'CLIENTE INFORMACION', 'F001-0878', 'C001-0876','0938484','7585743']
        comisionTable.row.add(nuevaFila).draw();
        */
    }

})