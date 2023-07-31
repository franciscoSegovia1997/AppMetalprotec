document.addEventListener('DOMContentLoaded',()=>{

    let btnFiltrarProductos = document.getElementById('filtrarProductos')
    btnFiltrarProductos.addEventListener('click',modificarTablaProductos)
    
    let pieProductos = document.getElementById('pieProductos')

    let pieGrafProductos = new Chart(pieProductos, {
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


    fetch('/statisticsMetalprotecproductsStatistics?qtInfo=15&timeInfo=0')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        tablaProductos = document.getElementById('tablaProductos')
        tablaProductos.innerHTML=''
        for(var i = 0; i < data.infoProducts.length; i++)
        {
            let nuevaFila = `
                    <tr>
                        <td>${data.infoCodes[i]}</td>
                        <td>${data.infoProducts[i]}</td>
                        <td class='text-end'>${data.infoValues[i]}</td>
                    </tr>`;
            tablaProductos.innerHTML += nuevaFila
        }
        pieGrafProductos.data.labels = data.infoProducts.slice(0,15)
        pieGrafProductos.data.datasets[0].data = data.infoValues.slice(0,15)
        pieGrafProductos.update()
    })


    function modificarTablaProductos()
    {
        let filtroProductos = document.getElementById('filtroProductos')
        let mesesProductos = document.getElementById('mesesProductos')
        let tablaProductos = document.getElementById('tablaProductos')

        fetch(`/statisticsMetalprotecproductsStatistics?qtInfo=${filtroProductos.value}&timeInfo=${mesesProductos.value}`)
        .then(response => response.json())
        .then(data => {
            tablaProductos.innerHTML = ''
            for(var i = 0; i < data.infoProducts.length; i++)
            {
                let nuevaFila = `
                        <tr>
                            <td>${data.infoCodes[i]}</td>
                            <td>${data.infoProducts[i]}</td>
                            <td class='text-end'>${data.infoValues[i]}</td>
                        </tr>`;
                tablaProductos.innerHTML += nuevaFila
            }
            pieGrafProductos.data.labels = data.infoProducts.slice(0,Number(`${filtroProductos.value}`))
            pieGrafProductos.data.datasets[0].data = data.infoValues.slice(0,Number(`${filtroProductos.value}`))
            pieGrafProductos.update()
        })
    }
})