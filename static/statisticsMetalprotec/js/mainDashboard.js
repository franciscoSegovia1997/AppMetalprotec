document.addEventListener('DOMContentLoaded',()=>{

    let btnFiltrarClientes = document.getElementById('filtrarClientes')
    btnFiltrarClientes.addEventListener('click',modificarTablaClientes)

    let btnFiltrarVentas = document.getElementById('filtrarVentas')
    btnFiltrarVentas.addEventListener('click',modificarTablaVentas)

    let pieClientes = document.getElementById('pieClientes')
    let grafVentas = document.getElementById('grafVentas')

    let pieGrafClientes = new Chart(pieClientes, {
        type: 'doughnut',
        data: {
            labels: [],
            datasets: [
                {
                backgroundColor: ["#FF0000", "#00FF00","#0000FF","#FF00FF","#00FFFF",'#FFFF00','#70db93','#5c3317','#9f5f9f','#b5a642','#a62a2a','#7093db','#871f78','#238e23','#dbdb70'],
                data: []
                }
            ]
        },
    })

    let tablaVentas = new Chart(grafVentas,{
        type:'bar',
        options:{
            scales:{
                x:{
                    grid:{
                        display: false,
                    },
                },
                y:{
                    grid:{
                        display: false,
                    },
                },
            },
        },
        data:{
            labels:[],
            datasets:[{
                label:'Soles',
                backgroundColor:'#0275d8',
                data:[],
            },
            {
                label:'Dolares',
                backgroundColor:'red',
                data:[],
            }]
        }
    })

    fetch('/statisticsMetalprotecsalesxMonths?monthInfo=10')
    .then(response => response.json())
    .then(data => {
        tablaVentas.data.labels = data.monthList.slice(0,10)
        tablaVentas.data.datasets[0].data = data.salesSoles.slice(0,10)
        tablaVentas.data.datasets[1].data = data.salesDollars.slice(0,10)
        tablaVentas.update()
    })

    fetch('/statisticsMetalprotecresumeSalesxYear?yearInfo=2023')
    .then(response => response.json())
    .then(data => {
        let filaAcumulado = document.getElementById('filaAcumulado')
        filaAcumulado.innerHTML = ''
        filaAcumulado.innerHTML += '<td>Acumulado</td>'
        let acumulado = 0
        let filaTotal = document.getElementById('filaTotal')
        filaTotal.innerHTML = ''
        filaTotal.innerHTML += '<td>Total</td>'
        let filaSoles = document.getElementById('filaSoles')
        filaSoles.innerHTML = ''
        filaSoles.innerHTML += '<td>Soles</td>'
        let filaDolares = document.getElementById('filaDolares')
        filaDolares.innerHTML = ''
        filaDolares.innerHTML += '<td>Dolares</td>'
        for(let i = 0; i < 12; i++)
        {
            acumulado = acumulado + Number(Number((Number(data.salesDollars[i])*Number(data.tcInfo)) + Number(data.salesSoles[i])).toFixed(2))
            filaSoles.innerHTML += `<td style="text-align:right;">${Number(data.salesSoles[i]).toLocaleString('es-MX')}</td>`
            filaDolares.innerHTML += `<td style="text-align:right;">${Number(data.salesDollars[i]).toLocaleString('es-MX')}</td>`
            filaTotal.innerHTML += `<td style="text-align:right;">${Number(Number((Number(data.salesDollars[i])*Number(data.tcInfo)) + Number(data.salesSoles[i])).toFixed(2)).toLocaleString('es-MX')}</td>`
            filaAcumulado.innerHTML += `<td style="text-align:right;">${acumulado.toLocaleString('es-MX')}</td>`
        }
    })

    fetch('/statisticsMetalprotecclientStatistics?qtInfo=15&timeInfo=0')
    .then(response => response.json())
    .then(data => {
        tablaClientes = document.getElementById('tablaClientes')
        tablaClientes.innerHTML = ''
        for(var i = 0; i < data.infoClientes.length; i++)
        {
            let nuevaFila = `
                    <tr>
                        <td>${data.infoRucs[i]}</td>
                        <td>${data.infoClientes[i]}</td>
                        <td class='text-end'>${data.infoValues[i]}</td>
                    </tr>`;
            tablaClientes.innerHTML += nuevaFila
        }
        pieGrafClientes.data.labels = data.infoClientes.slice(0,15)
        pieGrafClientes.data.datasets[0].data = data.infoValues.slice(0,15)
        pieGrafClientes.update()
    })

    function modificarTablaClientes()
    {
        let filtroClientes = document.getElementById('filtroClientes')
        let mesesClientes = document.getElementById('mesesClientes')
        let tablaClientes = document.getElementById('tablaClientes')

        fetch(`/statisticsMetalprotecclientStatistics?qtInfo=${filtroClientes.value}&timeInfo=${mesesClientes.value}`)
        .then(response => response.json())
        .then(data => {
            tablaClientes.innerHTML = ''
            for(var i = 0; i < data.infoClientes.length; i++)
            {
                let nuevaFila = `
                        <tr>
                            <td>${data.infoRucs[i]}</td>
                            <td>${data.infoClientes[i]}</td>
                            <td class='text-end'>${data.infoValues[i]}</td>
                        </tr>`;
                tablaClientes.innerHTML += nuevaFila
            }
            pieGrafClientes.data.labels = data.infoClientes.slice(0,Number(`${filtroClientes.value}`))
            pieGrafClientes.data.datasets[0].data = data.infoValues.slice(0,Number(`${filtroClientes.value}`))
            pieGrafClientes.update()
        })
    }

    function modificarTablaVentas()
    {
        let filtroVentas = document.getElementById('filtroVentas')

        fetch(`/statisticsMetalprotecsalesxMonths?monthInfo=${filtroVentas.value}`)
        .then(response => response.json())
        .then(data => {
            tablaVentas.data.labels = data.monthList.slice(0,parseInt(filtroVentas.value))
            tablaVentas.data.datasets[0].data = data.salesSoles.slice(0,parseInt(filtroVentas.value))
            tablaVentas.data.datasets[1].data = data.salesDollars.slice(0,parseInt(filtroVentas.value))
            tablaVentas.update()
        })
    }
})


function recargarResumen()
{
    let filtroResumen = document.getElementById('filtroResumenVentas')
    fetch(`/statisticsMetalprotecresumeSalesxYear?yearInfo=${filtroResumen.value}`)
    .then(response => response.json())
    .then(data => {
        let filaAcumulado = document.getElementById('filaAcumulado')
        filaAcumulado.innerHTML = ''
        filaAcumulado.innerHTML += '<td>Acumulado</td>'
        let acumulado = 0
        let filaTotal = document.getElementById('filaTotal')
        filaTotal.innerHTML = ''
        filaTotal.innerHTML += '<td>Total</td>'
        let filaSoles = document.getElementById('filaSoles')
        filaSoles.innerHTML = ''
        filaSoles.innerHTML += '<td>Soles</td>'
        let filaDolares = document.getElementById('filaDolares')
        filaDolares.innerHTML = ''
        filaDolares.innerHTML += '<td>Dolares</td>'
        for(let i = 0; i < 12; i++)
        {
            acumulado = acumulado + Number(Number((Number(data.salesDollars[i])*Number(data.tcInfo)) + Number(data.salesSoles[i])).toFixed(2))
            filaSoles.innerHTML += `<td style="text-align:right;">${Number(data.salesSoles[i]).toLocaleString('es-MX')}</td>`
            filaDolares.innerHTML += `<td style="text-align:right;">${Number(data.salesDollars[i]).toLocaleString('es-MX')}</td>`
            filaTotal.innerHTML += `<td style="text-align:right;">${Number(Number((Number(data.salesDollars[i])*Number(data.tcInfo)) + Number(data.salesSoles[i])).toFixed(2)).toLocaleString('es-MX')}</td>`
            filaAcumulado.innerHTML += `<td style="text-align:right;">${acumulado.toLocaleString('es-MX')}</td>`
        }
    })

}