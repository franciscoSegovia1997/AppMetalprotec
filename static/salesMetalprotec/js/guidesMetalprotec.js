document.addEventListener('DOMContentLoaded', ()=>{
    $('#guidesTable').DataTable({
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

function createInvoiceFromGuides()
{
    selectedGuides = document.querySelectorAll('.selectedGuide')
    guidesInfo = []
    for(var i = 0; i < selectedGuides.length; i++)
    {
        if(selectedGuides[i].firstChild.checked === true)
        {
            guidesInfo.push(selectedGuides[i].id)
        }
    }

    if(guidesInfo.length > 0)
    {
        dataGuides = {
            'guidesInfo':guidesInfo
        }

        fetch('/salesMetalproteccreateInvoiceFromGuides',{
            method:"POST",
            headers:
            {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body:JSON.stringify(dataGuides)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })

        window.location.href = '/salesMetalprotecguidesMetalprotec'
    }
    else
    {
        window.location.href = '/salesMetalprotecguidesMetalprotec'
    }

}


function createBillFromGuides()
{
    selectedGuides = document.querySelectorAll('.selectedGuide')
    guidesInfo = []
    for(var i = 0; i < selectedGuides.length; i++)
    {
        if(selectedGuides[i].firstChild.checked === true)
        {
            guidesInfo.push(selectedGuides[i].id)
        }
    }

    if(guidesInfo.length > 0)
    {
        dataGuides = {
            'guidesInfo':guidesInfo
        }

        fetch('/salesMetalproteccreateBillFromGuides',{
            method:"POST",
            headers:
            {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body:JSON.stringify(dataGuides)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })

        window.location.href = '/salesMetalprotecguidesMetalprotec'
    }
    else
    {
        window.location.href = '/salesMetalprotecguidesMetalprotec'
    }

}


function getCookie(name) 
{
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") 
    {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) 
        {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) 
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}