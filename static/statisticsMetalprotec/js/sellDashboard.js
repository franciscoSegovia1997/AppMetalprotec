document.addEventListener('DOMContentLoaded',()=>{

    let btnFiltrarVentas = document.getElementById('filtrarVentas')
    btnFiltrarVentas.addEventListener('click',modificarTablaVentas)

    let btnFiltrarVendedoresTiempo = document.getElementById('filtrarVendedoresTiempo')
    btnFiltrarVendedoresTiempo.addEventListener('click',modificarTablaVendedoresTiempo)

    let btnFiltrarVendedor = document.getElementById('filtrarVendedor')
    btnFiltrarVendedor.addEventListener('click',modificarTablaVendedor)

    let grafVentas = document.getElementById('grafVentas')
    let grafVendedor = document.getElementById('grafVendedor')
    let grafVendedoresTiempo = document.getElementById('grafVendedoresTiempo')

    let tablaVendedoresTiempo = new Chart(grafVendedoresTiempo,{
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
            labels:['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
            datasets:[{
                label:'V1',
                backgroundColor:'#0275d8',
                data:[],
            },
            {
                label:'V2',
                backgroundColor:'#FF0000',
                data:[],
            },
            {
                label:'V3',
                backgroundColor:'#00FF00',
                data:[],
            },
            {
                label:'V4',
                backgroundColor:'#FF00FF',
                data:[],
            },
            {
                label:'V5',
                backgroundColor:'#00FFFF',
                data:[],
            },
            {
                label:'V6',
                backgroundColor:'#FFFF00',
                data:[],
            }]
        }
    })

    let tablaVendedor = new Chart(grafVendedor,{
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

    fetch('/statisticsMetalprotecsellerStatistics?qtInfo=10&timeInfo=0')
    .then(response => response.json())
    .then(data => {
        tablaVendedor.data.labels = data.sellerCode.slice(0,10)
        tablaVendedor.data.datasets[0].data = data.sellerSoles.slice(0,10)
        tablaVendedor.data.datasets[1].data = data.sellerDollars.slice(0,10)
        tablaVendedor.update()
    })

    fetch('/statisticsMetalprotecsalesxMonths?monthInfo=10')
    .then(response => response.json())
    .then(data => {
        tablaVentas.data.labels = data.monthList.slice(0,10)
        tablaVentas.data.datasets[0].data = data.salesSoles.slice(0,10)
        tablaVentas.data.datasets[1].data = data.salesDollars.slice(0,10)
        tablaVentas.update()
    })

    fetch('/statisticsMetalprotecsellerSalesTime?yearInfo=2022&currencyInfo=SOLES')
    .then(response => response.json())
    .then(data => {
        console.log(datta)
        for(var i = 0; i < data.codeSeller.length; i++)
        {
            tablaVendedoresTiempo.data.datasets[i].label = data.codeSeller[i]
            tablaVendedoresTiempo.data.datasets[i].data = data.salesSeller[i]
        }
        tablaVendedoresTiempo.update()
    })

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

    function modificarTablaVendedoresTiempo()
    {
        let filtroVendedoresMoneda = document.getElementById('filtroVendedoresMoneda')
        let filtroVendedoresTiempo = document.getElementById('filtroVendedoresTiempo')
        fetch(`/statisticsMetalprotecsellerSalesTime?yearInfo=${filtroVendedoresTiempo.value}&currencyInfo=${filtroVendedoresMoneda.value}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            for(var i = 0; i < 6; i++)
            {
                tablaVendedoresTiempo.data.datasets[i].label = ''
                tablaVendedoresTiempo.data.datasets[i].data = []
            }
            for(var i = 0; i < data.codeSeller.length; i++)
            {
                tablaVendedoresTiempo.data.datasets[i].label = data.codeSeller[i]
                tablaVendedoresTiempo.data.datasets[i].data = data.salesSeller[i]
            }
            tablaVendedoresTiempo.update()
        })
    }

    function modificarTablaVendedor()
    {
        let filtroVendedor = document.getElementById('filtroVendedor')
        let mesesVendedor = document.getElementById('mesesVendedor')

        fetch(`/statisticsMetalprotecsellerStatistics?qtInfo=${filtroVendedor.value}&timeInfo=${mesesVendedor.value}`)
        .then(response => response.json())
        .then(data => {
            tablaVendedor.data.labels = data.sellerCode.slice(0,parseInt(filtroVendedor.value))
            tablaVendedor.data.datasets[0].data = data.sellerSoles.slice(0,parseInt(filtroVendedor.value))
            tablaVendedor.data.datasets[1].data = data.sellerDollars.slice(0,parseInt(filtroVendedor.value))
            tablaVendedor.update()
        })
    }
})