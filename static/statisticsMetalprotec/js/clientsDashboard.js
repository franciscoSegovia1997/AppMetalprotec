document.addEventListener('DOMContentLoaded',()=>{

    let btnFiltrarClientes = document.getElementById('filtrarClientes')
    btnFiltrarClientes.addEventListener('click',modificarTablaClientes)

    let pieClientes = document.getElementById('pieClientes')

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
})